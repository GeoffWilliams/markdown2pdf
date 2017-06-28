# Markdown2PDF

Markdown2pdf is python command line tool to convert markdown files to pdf

## Installation

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
