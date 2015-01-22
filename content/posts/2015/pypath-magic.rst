=================
pypath-magic v0.3
=================

:tags: IPython, python, CLI
:date: 2015-01-21


``pypath`` command-line interface in ``pypath-magic`` v0.3
==========================================================

``pypath-magic`` provides a simple interface for adding modules and packages
to your Python path.

Unlike modifications to ``sys.path``, this allows you to easily modify your
Python path across sessions. Unlike modifications to environment variables,
this doesn't require you to explain to users, students, and colleagues *how* to
modify environment variables.

In addition to the namesake IPython magic, version 0.3 of ``pypath-magic`` adds
a command-line interface (CLI) that resembles the IPython interface. After
installing the latest version (``pip install pypath_magic``), you'll have
access to a ``pypath`` command in your favorite terminal/shell.

You might also want to take a look at the original
`quick-start article <http://tonysyu.github.io/pypath-magic.html>`_ for
version 0.2. The rest of this article just translates the IPython workflow
from that article to the new CLI.


Why would you modify your Python path?
======================================

You're a pragmatic Python developer, so you extract the logically related bits
of your code into functions and group those functions together into modules.

Now, **how do you actually import those modules**? If you're in the directory
containing those modules, you're good to go:

.. code-block:: bash

   $ ls  # Helper files are in the same directory as the main script.
   data_wranglers.py
   main.py
   plot_helpers.py


Now, if you want to execute a main script that needs to wrangle some data and
plot the results, then you can just run:

.. code-block:: bash

   $ python main.py
   [Success]

If, instead, those files are located elsewhere, you might get something like
this:

.. code-block:: bash

   $ ls                   # Main file is local ...
   main.py
   path/

   $ ls path/to/my-utils  # ...but utilities are somewhere else.
   data_wranglers.py
   plot_helpers.py

   $ python main.py

   Traceback (most recent call last):
     File "scratch.py", line 1, in <module>
       import plot_helpers
   ImportError: No module named plot_helpers


Quickfix: ``sys.path``
----------------------

The quick fix here is to append to ``sys.path`` in ``main.py``:

.. code-block:: python

   import sys
   sys.append('path/to/my-utils')

   from plot_helpers import plot_slope_marker

**But**, if you want to use these utilities elsewhere, you'll have to jump
through these hoops every time you use it.


Persistent changes to your path
-------------------------------

To make persistent changes to your Python path, you'll have to
`tweak your PYTHONPATH`_ or figure out how to `add '*.pth' files to your
site-packages directory`_. Sure, you can package up your code properly, but
for most people, that's a significant leap in effort.

These solutions are annoying for most users and downright intimidating to newer
developers. With ``pypath``, you can easily manipulate your Python path from
IPython_.


How to use the ``pypath`` CLI
=============================

After installing the latest version (``pip install pypath_magic``), you'll have
access to a ``pypath`` command in your favorite terminal/shell.


List the custom paths
---------------------

To list all the custom paths added by ``pypath``, open a terminal and type:

.. code-block:: bash

   $ pypath

When you get started, you won't have anything there, so you'll get:

.. code-block:: bash

   No user paths are defined.
   See `pypath -h` for usage information.


Add to your Python path
-----------------------

To add some custom paths, just change to a directory and call ``pypath add``:

.. code-block:: bash

   $ cd path/to/my-utils

   $ ls
   data_wranglers.py
   plot_helpers.py

   $ pypath add
   Added u'/absolute/path/to/my-utils' to path.

   $ pypath
   0. /absolute/path/to/my-utils

Now you can reuse those helper functions from anywhere:

.. code-block:: python

   from plot_helpers import plot_slope_marker


Deleting one of your custom paths
---------------------------------

If you later want to delete a directory from your path, just use
``pypath delete``:

.. code-block:: bash

   $ cd path/to/my-utils

   $ pypath delete
   Deleted u'/absolute/path/to/my-utils' from path.


List everything in your Python path
-----------------------------------

You can also list your entire Python path with ``pypath list-all``:

.. code-block:: bash

   $ pypath list-all

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

.. code-block:: bash

   $ pypath add path/to/useful-modules
   Added u'/absolute/path/to/useful-modules' to path.

   $ pypath add /absolute/path/to/stuff
   Added u'/absolute/path/to/stuff' to path.

   $ pypath add path/to/things
   Added u'/absolute/path/to/things' to path.

   $ pypath
   0. /absolute/path/to/useful-modules
   1. /absolute/path/to/stuff
   2. /absolute/path/to/things


Notice those numbers in the list above. We can use those indices to delete
paths, or we can delete using string paths:

.. code-block:: bash

   $ pypath delete 1
   Deleted u'/absolute/path/to/stuff' from path.

   $ pypath
   0. /absolute/path/to/useful-modules
   1. /absolute/path/to/things

   $ pypath delete path/to/useful-modules
   Deleted u'/absolute/path/to/useful-modules' from path.

   $ pypath
   0. /absolute/path/to/things


How it works
============

The basic idea is really simple: The ``pypath`` command just maintains a custom
``*.pth`` file in your site-packages directory. Altering that file alters the
paths in the Python path. Since this is a custom ``*.pth`` file, you don't have
to worry about screwing up packages installed by other means.


Install
=======

To install using pip, just type the following in a terminal:

.. code-block:: bash

   $ pip install pypath_magic

Or if you're feeling lucky:

.. code-block:: bash

   $ pip install git+https://github.com/tonysyu/pypath-magic

Or if you want to go `direct to the source`_:

.. code-block:: bash

   $ git clone https://github.com/tonysyu/pypath-magic.git
   $ cd pypath-magic
   $ python setup.py install


Dependencies
============

* Python 2.7/3.4 (older versions probably work, but this is not tested)
* IPython >= 1.0


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
.. _direct to the source: https://github.com/tonysyu/pypath-magic
