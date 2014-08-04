============
pypath-magic
============

:tags: IPython, python
:date: 2014-08-04


``%pypath``: An IPython magic for manipulating your Python path
===============================================================

So you're finally starting to write reusable code---extracting logically
related bits into functions and grouping those functions together into modules.

Now, **how do you actually import those modules**? If you're in the directory containing those modules, you're good to go:

.. code-block:: python

   In [1]: %ls  # Desired files are in the same directory.
   data_wranglers.py
   plot_helpers.py

   In [2]: from plot_helpers import plot_slope_marker
   [Success]

If, instead, those files are located elsewhere, you might get something like
this:

.. code-block:: python

   In [3]: %ls path/to/my-utils  # Desired files are somewhere else.
   data_wranglers.py
   plot_helpers.py

   In [4]: from plot_helpers import plot_slope_marker
   ---------------------------------------------------------------------------
   ImportError                               Traceback (most recent call last)
   <ipython-input-141-1d0fef5fa475> in <module>()
   ----> 1 from plot_helpers import plot_slope_marker

   ImportError: No module named plot_helpers


``sys.path``
------------

The quick fix here is to append to ``sys.path``:


.. code-block:: python

   In [3]: import sys

   In [4]: sys.append('path/to/my-utils')

   In [5]: from plot_helpers import plot_slope_marker
   [Success]

**But**, the next time you fire up python, you get the same ``ImportError`` we
saw before.


Persistent changes to your path
-------------------------------

To make persistent changes to your Python path, you'll have to
`tweak your PYTHONPATH`_ or figure out how to `add '*.pth' files to your
site-packages directory`_.

These solutions are annoying for most users and downright intimidating to newer
developers. ``pypath`` provides a simple solution for manipulating your
Python path from IPython_.


How to use ``pypath-magic``
===========================

The ``pypath-magic`` `module <https://github.com/tonysyu/pypath-magic>`_ adds
an `IPython magic`_ (err... Jupyter_ magic?) command for easily manipulating
your Python path.


Load the extension
------------------

To use the magic command, just load the extension from an IPython session:

.. code-block:: python

   In [1]: %load_ext pypath_magic


List the custom paths
---------------------

After loading, you will have access to the ``%pypath`` magic. You can type:

.. code-block:: python

   In [2]: %pypath

to list all the custom paths added by ``pypath-magic``. When you get started,
you won't have anything there.


Add to your Python path
-----------------------

To add some custom paths, just change to a directory and call ``%pypath -a``:

.. code-block:: python

   In [3]: %cd path/to/my-utils

   In [4]: %ls
   data_wranglers.py
   plot_helpers.py

   In [5]: %pypath -a
   Added u'/absolute/path/to/my-utils' to path.

   In [6]: %pypath
   0. /absolute/path/to/my-utils

Now you can reuse those helper functions from anywhere:

.. code-block:: python

   In [7]: from plot_helpers import plot_slope_marker

Changes to your Python path will persist across IPython sessions, and those
paths will be available outside of IPython.


Deleting one of your custom paths
---------------------------------

If you later want to delete a directory from your path, just use
``%pypath -d``:

.. code-block:: python

   In [8]: %cd path/to/my-utils

   In [9]: %pypath -d
   Deleted u'/absolute/path/to/my-utils' from path.


List everything in your Python path
-----------------------------------

You can also list your entire Python path with ``%pypath -l``:

.. code-block:: python

   In [10]: %pypath -l

   /Users/tonysyu/code/yutils
   /Users/tonysyu/code/skimage
   /Users/tonysyu/code/mpl/lib
   /Users/tonysyu/code/ipython
   /Users/tonysyu/code/deli
   /Users/tonysyu/code/mpltools
   /Applications/Canopy.app/appdata/canopy-1.4.1.1975.macosx-x86_64/Canopy.app/Contents/lib/python27.zip
   /Applications/Canopy.app/appdata/canopy-1.4.1.1975.macosx-x86_64/Canopy.app/Contents/lib/python2.7
   ...
   /absolute/path/to/my-utils


Adding and deleting using arguments
-----------------------------------

Finally, you can manipulate paths---without changing to those directories---by
passing arguments to the add and delete commands.

First we add paths using relative or absolute directory paths:

.. code-block:: python

   In [11]: %pypath -a path/to/useful-modules
   Added u'/absolute/path/to/useful-modules' to path.

   In [12]: %pypath -a /absolute/path/to/stuff
   Added u'/absolute/path/to/stuff' to path.

   In [13]: %pypath -a path/to/things
   Added u'/absolute/path/to/things' to path.

   In [14]: %pypath
   0. /absolute/path/to/useful-modules
   1. /absolute/path/to/stuff
   2. /absolute/path/to/things


Notice those numbers in the list above. We can use those indices to delete
paths, or we can delete using string paths:

.. code-block:: python

   In [15]: %pypath -d 1

   In [16]: %pypath
   0. /absolute/path/to/useful-modules
   1. /absolute/path/to/things

   In [17]: %pypath -d path/to/stuff

   In [18]: %pypath
   0. /absolute/path/to/things


How it works
============

The basic idea is really simple: The ``pypath`` command just maintains a custom
``*.pth`` file in your site-packages directory. Altering that file alters the
paths in the Python path. Since this is a custom ``*.pth`` file, you don't have
to worry about screwing up packages installed by other means.


Install
=======

To install using pip, just type the following in a terminal::

   $ pip install pypath_magic

Or if you're feeling lucky::

   $ pip install git+https://github.com/tonysyu/pypath-magic

Or if you <3 github::

   $ git clone https://github.com/tonysyu/pypath-magic.git
   $ cd pypath-magic
   $ python setup.py install


Dependencies
============

* Python 2.7
* IPython


License
=======

New BSD (a.k.a. Modified BSD). See LICENSE_ file in this directory for details.

.. _IPython:
   http://ipython.org
.. _tweak your PYTHONPATH:
   http://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath
.. _add '*.pth' files to your site-packages directory:
   https://docs.python.org/2/library/site.html#module-site
.. _IPython magic:
   http://ipython.org/ipython-doc/dev/interactive/tutorial.html#magic-functions
.. _Jupyter: http://jupyter.org/
.. _LICENSE: https://github.com/tonysyu/pypath-magic/blob/master/LICENSE
