=======================
Matplotlib named colors
=======================

:tags: matplotlib, color
:status: draft
:date: 2013-12-31


Most people just use a few of the most common colors; in particular, those with
single-character shortcuts:

   'b' = blue
   'g' = green
   'r' = red
   'c' = cyan
   'm' = magenta
   'y' = yellow
   'k' = black
   'w' = white

These colors are fine, but not ideal, for a number of use cases.  One way
around this limitation is to explicitly pass RGB values to any color parameter.
In this post, however, I'm going to focus on named colors.

You can actually use any of the `X11 colors`_ (web-safe colors?) in Matplotlib.
These colors are listed in the ``cnames`` dictionary of the ``colors`` module:

.. code-block:: python

   pass

Since it's a bit difficult to choose colors from such a big list, let's try to
sort and filter these colors.


Color metrics
=============

First, we need to figure out how to sort these colors. We can judge
a color by any number of different `color metrics`_, but let's focus on
luminance, hue, saturation, and value. HSV---hue, saturation, and value---is
commonly used as an alternative color representation. These metrics are
described thoroughly `elsewhere <http://en.wikipedia.org/wiki/HSL_and_HSV>`,
and Matplotlib actually provides a tool to convert RGB values to HSV:

.. code-block:: python

   pass

and the luminance can be converted from RGB values as:

.. code-block:: python

   pass

Hue
---

Hue corresponds to what we normally think of as color
(e.g. red, green, blue, etc.).

.. code-block:: python

   pass

Through trial and error, I found the following hues are fairly good at
distinguishing the colors

Saturation
----------

Roughly speaking, high saturation corresponds to intense colors, while low
saturation corresponds to muted colors.

Value and luminance
-------------------

value roughly corresponds to lightness (


Plotting a cheat sheet
======================

Weird grey values: http://en.wikipedia.org/wiki/Grey#Web_colors


Applications
============

Now, if you filter colors with some desired property, you can easily choose a set colors for a color cycle. Below is an example with a 7-color cycle with a luminance between 0.4 and 0.7.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots()
   cycle = ['tomato',
            'royalblue',
            'gray',
            'orange',
            'limegreen',
            'hotpink',
            'deepskyblue']
   ax.set_color_cycle(cycle)
   x = np.linspace(0, 10)
   for shift in np.arange(len(cycle)):
     ax.plot(x, np.sin(x + shift/2.))
   plt.show()

.. _X11 colors: http://en.wikipedia.org/wiki/Web_colors#X11_color_names
.. _color metrics: http://en.wikipedia.org/wiki/HSL_and_HSV

