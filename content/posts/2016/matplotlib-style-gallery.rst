========================
Matplotlib Style Gallery
========================

:tags: matplotlib
:date: 2016-03-29


This post is more than a year in the making (life got in the way), so this
isn't exactly hot off the press. I added support for style-sheets back in `Matplotlib 1.4
<http://matplotlib.org/1.4.2/users/whats_new.html#style-package-added>`__,
based on my implementation in
`mpltools <https://github.com/tonysyu/mpltools>`__ [1]_, and built a `gallery
page`_ to easily compare styles.

Style-sheets allow you to turn a plot that looks like this:

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.random.randn(1000, 3)

   plt.hist(x, 10)
   plt.show()

.. image:: {filename}/images/posts/2016/hist-plot-defaults.png

Into a plot that looks like this:

.. code-block:: python

   plt.style.use('ggplot')
   plt.hist(x, 10)
   plt.show()

.. image:: {filename}/images/posts/2016/hist-plot-ggplot.png


Currently, there are only a handful of style-sheets included with Matplotlib,
but even now, it may be difficult to choose between what's available [2]_.
For easier comparison, I've created a `gallery page`_ to easily compare existing
style-sheets:

.. image:: {filename}/images/posts/2016/style-gallery-snap-shot.png
   :target: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

You can select a given plot to zoom in and navigate between zoomed in plots
with arrow keys.

This page disables user input, but the actual gallery app
(`github repo <https://github.com/tonysyu/matplotlib-style-gallery>`__)
also allows you to compare custom style-sheets by passing a URL, or explicitly
defining a style sheet
(using `matplotlibrc syntax <http://matplotlib.org/users/customizing.html>`__).


.. [1] https://github.com/matplotlib/matplotlib/pull/2236
.. [2] https://github.com/matplotlib/matplotlib/pull/3190

.. _gallery page: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
