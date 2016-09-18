Markdown2PDF
============

Markdown2pdf is python command line tool to convert markdown files to pdf

Installation
------------

Install Markdown2PDF with pip

.. code-block:: shell

    pip install git+https://github.com/lynnco/markdown2pdf.git


Usage
-----

Use via the command ``md2pdf``

.. code-block:: shell

    md2pdf resume.md

You can also appoint a theme by argument ``--theme``

.. code-block:: shell

    md2pdf resume.md --theme=github

Or, you can even using your self defined theme

.. code-block:: shell

    md2pdf resume.md --theme=path_to_style.css

Contains these default themes

* github (from GitHub.Inc)

* solarized-dark (from mixu/markdown-styles)

* ghostwriter (from mixu/markdown-styles)


Trouble shooting
----------------

1. ``ffi.h no such file or directory``

.. code-block:: shell

    apt-get install libffi-dev

2. ``OSError: library not found: 'libcairo.so.2'``

.. code-block:: shell

    brew install cairo pango gdk-pixbuf libxml2 libxslt libffi

(from: https://github.com/Kozea/WeasyPrint/issues/79)
