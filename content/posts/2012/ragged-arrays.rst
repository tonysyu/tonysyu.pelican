=============
Ragged arrays
=============

:tags: numpy, io, data
:date: 2012-05-27


I often need to save a series of arrays in which *one* dimension varies in
length---sometimes called a ragged array [1]_. For example, I'm running
particle tracking experiments, and I need to save the 2D coordinates of all
particles in each video frame. The number of particles in each frame will vary
due to movement across the edges of the frame and velocity components normal to
the focal plane; so, I can't simply save a (dense) 3D array. Instead, I just
store this data in a Python list of ``N``-by-2 numpy arrays, where ``N`` is the
number of particles in a frame and varies for each array.

The question is: How do you save this list of arrays? In my first attempt,
I saved each array individually (as separate keys in an `.npz file`_); this
approach gave slow save/load times and larger file sizes. A better approach is
to stack all the ragged arrays along the dimension that varies in
length---i.e.  the ragged dimension. Then, I use numpy's `.npz file`_ to save
the array data.


Stacking and splitting arrays
=============================

numpy provides a number of functions to stack arrays: concatenate_, hstack_,
vstack_, and dstack_. The main difference here is that we want to save the
starting indices of the sub-arrays so that we can slice them back out later:

.. code-block:: python

   import numpy as np

   def stack_ragged(array_list, axis=0):
       lengths = [np.shape(a)[axis] for a in array_list]
       idx = np.cumsum(lengths[:-1])
       stacked = np.concatenate(array_list, axis=axis)
       return stacked, idx

This returns the stacked array and the starting index of each sub-array. To use
`stack_ragged`, just pass in a list of arrays:

.. code-block:: python

    >>> array_list = [np.array([(0, 0), (1, 1)]),
    ...               np.array([(2, 2), (3, 3), (4, 4)]),
    ...               np.array([(5, 5)])]
    >>> stacked, idx = stack_ragged(array_list)
    >>> print idx
    [2 5]
    >>> print stacked
    [[0 0]
     [1 1]
     [2 2]
     [3 3]
     [4 4]
     [5 5]]

Here, the ragged arrays are stacked vertically, since ``axis = 0`` by default.

To split up this array back into a list of ragged arrays, just pass in the
stacked array and the starting indices (and the axis, if necessary) to numpy's
split_ function:

.. code-block:: python

    >>> for array in np.split(stacked, idx):
    ...     print array
    [[0 0]
     [1 1]]
    [[2 2]
     [3 3]
     [4 4]]
    [[5 5]]

which returns our original list of arrays. (Note: the loop is just for prettier
printing.)


Saving and loading
==================

So stacking turns our list of arrays into a single array, which we can easily
save using numpy's save_ (single array) or savez_ (``dict`` of arrays)
functions. If we want to get back our original arrays, however, we also need to
save the start indices:

.. code-block:: python

   def save_stacked_array(fname, array_list, axis=0):
       stacked, idx = stack_ragged(array_list, axis=axis)
       np.savez(fname, stacked_array=stacked, stacked_index=idx)

Finally, we define a function to load our original list of arrays:

.. code-block:: python

   def load_stacked_arrays(fname, axis=0):
       npzfile = np.load(fname)
       idx = npzfile['stacked_index']
       stacked = npzfile['stacked_array']
       return np.split(stacked, idx, axis=axis)

Alternatively, the save function could store the stacking-axis in the .npz file
so that you don't have to specify it in the load function. Another improvement
would be to guess the stacking axis in ``stack_ragged`` by checking which axis
varies in size (this would fail, however, for constant ``N``). And finally, you
can use savez_compressed_ instead of savez_ to reduce storage.

P.S. After implementing this approach, I learned that NetCDF_ files support
ragged arrays out of the box (using `VLEN types`_)---it's not the first time
I've reinvented the wheel; it won't be the last.


.. [1] http://mail.scipy.org/pipermail/numpy-discussion/2011-March/055208.html

.. _.npz file:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html
.. _concatenate:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html
.. _hstack:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.hstack.html
.. _vstack:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html
.. _dstack:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.dstack.html
.. _split:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.split.html
.. _save:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html
.. _savez:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html
.. _savez_compressed:
   http://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html
.. _NetCDF:
   http://en.wikipedia.org/wiki/NetCDF
.. _VLEN types:
   http://www.unidata.ucar.edu/software/netcdf/docs/netcdf/User-Defined-Types.html

