******
Readme
******

:author: Tony S. Yu

Basic Use
=========

This website is built using `Pelican`_.  Pages are written in either
`Markdown`_ (a.k.a. "md") or `reStructureText`_ (a.k.a. "rst"). To generate
html, just run:

    pelican path/to/content

This command renders html files to a directory called "output", which is
a self-contained version of the website.


Customization
=============

For a customized website, you should create a theme and use custom settings.
From the command line, you can call:

	pelican -t theme -s settings.py content

This assumes you're in a directory with a python file named "settings.py",
a subdirectory named "theme", and a subdirectory named "content" with all your
md and/or rst files. To learn more about themes, see the tutorial on how to
`create themes`_ for Pelican. In the settings file, you can define global
variables for use in templates (must be all caps), but there are also some
`settings variables`_ pre-defined by Pelican.


Blog Index
==========

Blog entries are displayed by the main index of the website (i.e., `{{ SITE_URL
}}/index.html`. Order of the entries is controlled by the `Jinja2`_ template `theme/index.html`.


Static vs Blog Pages
====================

Any md and/or rst files put into the "pages" directory of the "content"
directory will be rendered as a static html page and, by convention, *not*
added to the main index (this could be overridden in the index template,
however).


.. _Pelican: http://readthedocs.org/docs/pelican/en/
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _create themes: http://readthedocs.org/docs/pelican/en/2.7.2/themes.html
.. _settings variables: http://readthedocs.org/docs/pelican/en/latest/settings.html
.. _Jinja2: http://jinja.pocoo.org/docs/
