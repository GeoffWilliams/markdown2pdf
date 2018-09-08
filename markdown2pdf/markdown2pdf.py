#!/usr/bin/env python

import argparse
import os




# nasty hack
os.environ["WEASYPRINT_USE_PDFRW"] = "yes"





import mistune
import re
from mistune_contrib.highlight import HighlightMixin
from mistune_contrib.toc import TocMixin
import weasyprint


class CustomRenderer(HighlightMixin, TocMixin, mistune.Renderer):
    pass

def read_file(filename):
    with open(filename, 'r') as file:
        txt = file.read()

    return txt


def scandir(basedir):
  files = []
  for l in os.listdir(basedir):
    path = os.path.join(basedir, l)
    if os.path.isdir(path):
      if not l.startswith("."):
        for found in scandir(path):
          files.append(found)
    elif l.endswith(".md"):
      files.append(path)

  return files


def convert_md_2_pdf(filename, output=None, theme=None, line_numbers=None, debug=None, no_toc=None, footer_fragment=None):
    pagebreak = """<div style="page-break-after: always;">&nbsp;</div>"""
    first_style = """ class="firstpage" """
    nasty_hack_footer = """<footer class="nasty_hack_footer">&nbsp;</footer>"""

    if os.path.isfile(footer_fragment):
        footer_xml = read_file(footer_fragment)
    else:
        print("no footer!")
        footer_xml = "&nbsp";


    mdtxt = ""
    if os.path.isdir(filename):
        # load all images relative to the top level directory
        basedir = filename
        print("processing directory")
        for work_file in scandir(filename):
            print("processing: %s" % work_file)
            mdtxt += read_file(work_file)
    else:
        # recursively process a directory
        mdtxt = read_file(filename)

        # load all images relative to the file
        basedir = os.path.dirname(filename)

    md_split = re.split(pagebreak, mdtxt, 1)

    if len(md_split) > 1:
        # we have a cover page...

        # cover - dont want TOC, use basic renderer
        markdown = mistune.Markdown()
        html_cover = markdown(md_split[0])
        body_index = 1
    else:
        print("no cover avaiable")
        html_cover = ""
        body_index = 0

    # body - do want TOC, use fully sick renderer
    custom_renderer = CustomRenderer()
    custom_renderer.options = {
        "linenos": line_numbers
    }

    markdown = mistune.Markdown(renderer=custom_renderer)
    custom_renderer.reset_toc()
    html_body = markdown(md_split[body_index])

    # ^^^^^  Markdown  ^^^^^
    # ======================
    # VVVVV    HTML    VVVVV

    toc_html = custom_renderer.render_toc(level=4)
    html = nasty_hack_footer + html_cover + pagebreak + html_body


    # Easiest/only way to do firstpage formatting in HTML/CSS seems to be to postprocess
    # everything _before_ the first matching pagebreak div
    html_post = []
    first_page = True
    c = 0
    for line in html.split("\n"):

        if pagebreak in line:
            if not no_toc and first_page:
                html_post.append(pagebreak)
                html_post.append(toc_html)
            first_page = False

        if first_page:
            if re.match(r"<[^/]+>", line):
                # add class="firstpage" to all elements on first page..
                line = re.sub(r"(<[^/]+)>", r"\1 " + first_style + ">", line)

        html_post.append(line)
        c += 1
    html_post.append(footer_xml)

    html_str = "\n".join(html_post)

    if debug:
        print(html_str)

    if not output:
        output = '.'.join([filename.rsplit('.')[0], 'pdf'])

    if not os.path.exists(theme):
        theme = os.path.join(
            os.environ.get('VIRTUAL_ENV', ''),
            os.path.dirname(__file__),
            'themes/' + theme + '.css',
        )

    # ^^^^^    HTML    ^^^^^
    # ======================
    # VVVVV    PDF     VVVVV
    weasyprint.HTML(string=html_str, base_url=basedir).write_pdf(
        output,
        stylesheets=[theme, "/home/geoff/sourced/pygments-css/default.css"]
    )


def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown file to pdf')
    parser.add_argument('filename', help='Markdown file name or directory')
    parser.add_argument(
        '--theme',
        help='Set the theme, default is GitHub flavored.',
        default='github'
    )
    parser.add_argument(
        '--output',
        help='''
            The output file name. If not set, the name will
            be same as the input file but with ".pdf".
        '''
    )
    parser.add_argument(
        '--line-numbers',
        help='Use line numbers for code samples',
        action='store_const',
        const="inline",
        default=False
    )
    parser.add_argument(
        '--debug',
        help='Use line numbers for code samples',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--no-toc',
        help='no table of contents',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--footer-fragment',
        help='Footer HTML (XML) fragment - default is to read footer.xml from current dir',
        default="footer.xml"
    )
    args = parser.parse_args()
    convert_md_2_pdf(**dict(args._get_kwargs()))


main()
