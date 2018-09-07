# Markdown2PDF

Markdown2pdf is python command line tool to convert markdown files to pdf

## Installation

## Hacky hack hack mchacky hack
```

# fix syntax crash, updated toc
pip3 install git+https://github.com/geoffwilliams/mistune-contrib.git

# fix page counters for TOC - fixes https://github.com/Kozea/WeasyPrint/pull/652
# use the next one for collective fix.. pip3 install git+https://github.com/Kozea/WeasyPrint

# the toc internal links all broken because of cairo bug
# https://github.com/Kozea/WeasyPrint/issues/678
# https://gitlab.freedesktop.org/cairo/cairo/issues/336
pip3 install git+https://github.com/Tontyna/WeasyPrint@patch_for_678

```

## Troubleshooting

Munted TOC?

Your headers `#` can only jump up/down one level at a time!

How to do my coversheet?

Normal markdown as you like, then the exact magic incantation:
<div style="page-break-after: always;">&nbsp;</div>

eg:
```markdown
# My Report
## My report that was done at great time and expense
Private and Confidential
<div style="page-break-after: always;">&nbsp;</div>
...rest of document here...
```


### OSX

```shell
brew install cairo pango gdk-pixbuf libxml2 libxslt libffi
```

### General

```shell
    pip install git+https://github.com/lynnco/markdown2pdf.git
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```

## Usage

Use via the command ``md2pdf``

```shell
    md2pdf resume.md
```

You can also appoint a theme by argument ``--theme``

```shell
    md2pdf resume.md --theme=github
```

Or, you can even using your self defined theme

```shell
    md2pdf resume.md --theme=path_to_style.css
```

Contains these default themes

* github (from GitHub.Inc)

* solarized-dark (from mixu/markdown-styles)

* ghostwriter (from mixu/markdown-styles)
