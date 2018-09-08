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

Where's my images - I'm doing a recursive document

Probably they are lost because the HTML generater has
no idea about the relative part of that path since it 
just gets one big glob of text to work with.

Solution:
1. always load images from `image`, eg `<img src="image/...`
2. For each directory that needs images, create a directory at the same
   level, like this:
   
```
├── foo
├── image
│   └── ...
└── basics
    └── bar
        ├── image
        │   └── ...
        └── baz.md
```

### Tips and tricks

#### Want a directory level heading?

00_index.md
```markdown
# Tada!
```

Now start all the other markdown files in the directory with
level 2 headings and they will be nicely grouped in output

#### Control output order
Just name your files into alphabetical order, numbers are a good trick here:

```shell
00_index.md
10_foo.md
20_bar.md
30_baz.md
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
