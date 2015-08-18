====
Code
====

I come from a background in scientific research, so most of my open source
contributions are related to data analysis and visualization in Python. That
said, my day job is no longer science and uses Perl, Javascript, and C#;
maybe I'll start having a bit more variety in the near future.


Personal projects
=================

- ``pypath-magic``: An IPython magic function, that turned into a command-line
  utility, for manipulating your Python path.
  (`CLI <https://tonysyu.github.io/pypath-magic-v03.html#.VdEVHVNViko>`__ |
  `IPython-magic <https://tonysyu.github.io/pypath-magic.html#.VdEVOVNViko>`__ |
  `github <https://github.com/tonysyu/pypath-magic>`__).

- ``matplotlib-style-gallery``: A simple gallery for viewing and comparing
  matplotlib style sheets
  (`static gallery <https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html>`__ |
  `github <https://github.com/tonysyu/matplotlib-style-gallery>`__).

- ``mpltools``: A collection of tools for working with `matplotlib`_ that I
  developed during my Ph.D. and postdoc. I don't actively develop it anymore,
  but I keep it around for posterity. The most interesting bits are a
  subpackage for manipulating visual styles (which was integrated into
  ``matplotlib.style``) and the plot2rst_ Sphinx extension, which I used for
  creating examples in ``scikit-image``.
  (`docs <https://tonysyu.github.io/mpltools/>`__ |
  `gallery <https://tonysyu.github.io/mpltools/auto_examples/index.html>`__ |
  `github <https://github.com/tonysyu/mpltools>`__).


Presentations
=============

- ``scikit-image`` tutorial at SciPy 2014.
  (`video <https://tonysyu.github.io/scikit-image-tutorial-at-scipy-2014.html>`__ |
  `notebooks <https://github.com/scikit-image/skimage-tutorials/tree/master/2014-scipy>`__)

- Lightening talk for ``scikit-image`` viewer at SciPy 2013.
  (`video <https://www.youtube.com/watch?v=ywHqIEv3xXg&feature=youtu.be&t=20m57s>`__ |
  `code <https://github.com/tonysyu/skimage-viewer-demo-Scipy2013>`__)


Contributions
=============

I've contributed to a number of open-source packages---particularly packages
in the scientific Python stack. Most of those contributions were bug fixes or
examples. A few of the more notable contributions are listed below.

`scikit-image`
--------------

Technically, I'm a core developer on the `scikit-image`_ project, but I haven't
contributed anything substantial recently because I don't do much image
processing these days.


- ``skimage.viewer`` package for interactive image processing and
  analysis using Qt
  (`demo <http://scikit-image.org/docs/dev/user_guide/viewer.html>`__ |
  `PR <https://github.com/scikit-image/scikit-image/pull/229>`__).

- ``label2rgb`` function for turning labeled images to false-color
  overlays (really useful for displaying segmentation results)
  (`demo <http://scikit-image.org/docs/dev/auto_examples/plot_join_segmentations.html>`__ |
  `PR <https://github.com/scikit-image/scikit-image/pull/485>`__).

- Improvements to ``scikit-image`` gallery allowing plots to be easily
  embedded in the documentation
  (`gallery <http://scikit-image.org/docs/dev/auto_examples/>`__ |
  `PR <https://github.com/scikit-image/scikit-image/pull/190>`__).

- Morphological reconstruction function
  (`demo <http://scikit-image.org/docs/dev/auto_examples/plot_holes_and_peaks.html>`__
  | `PR <https://github.com/scikit-image/scikit-image/pull/215>`__).

- Otsu thresholding function
  (`demo <http://scikit-image.org/docs/dev/auto_examples/plot_otsu.html>`__ |
  `commit <https://github.com/scikit-image/scikit-image/commit/fbbe38765d4afa7de1126540c31150a3ba94f862>`__).

`matplotlib`
------------

- ``matplotlib.style`` package for easily switching between style sheets
  in matplotlib
  (`demo <http://matplotlib.org/examples/style_sheets/plot_ggplot.html>`__ |
  `PR <https://github.com/matplotlib/matplotlib/pull/2236>`__).

- ``streamplot`` method/function for plotting streamlines
  (`demo <http://matplotlib.org/examples/images_contours_and_fields/streamplot_demo_features.html>`__ |
  `PR <https://github.com/matplotlib/matplotlib/pull/664>`__).

- ``LassoSelector`` for interactive data selection
  (`demo <http://matplotlib.org/examples/widgets/lasso_selector_demo.html>`__ |
  `PR <https://github.com/matplotlib/matplotlib/pull/730>`__).


.. _plot2rst: https://tonysyu.github.io/mpltools/auto_examples/sphinx/plot_plot2rst.html
.. _scikit-image: http://scikit-image.org/
.. _matplotlib: http://matplotlib.sourceforge.net/
