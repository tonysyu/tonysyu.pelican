=============================
Animating particles in a flow
=============================

:tags: matplotlib, sympy, scipy, mpltools, animation, fluids
:date: 2012-07-02


This article demonstrates matplotlib's animation_ module by animating marker
particles in a fluid flow around a cylinder. It's a bit long because it ties
together a number of different ideas:

- stream functions
- numerical integration
- plotting and animation

Before we really start, let's copy a function from a previous article on
`stream functions in potential flow`_.

.. code-block:: python

    import sympy
    from sympy.abc import x, y

    def velocity_field(psi):
        u = sympy.lambdify((x, y), psi.diff(y), 'numpy')
        v = sympy.lambdify((x, y), -psi.diff(x), 'numpy')
        return u, v

Here, ``velocity_field`` accepts a symbolic function, ``psi``, and returns
functions that calculate the velocity components for coordinates ``x`` and
``y``. Given a stream function ``psi``, we can calculate the velocity at any
point in space. For plotting, however, we need translate these velocities to
displacements; in other words, we need to integrate.


Calculating particle displacements
==================================

To calculate displacements from velocities, we need a `numerical integration`_
routine. Below, we wrap three integration functions:

- a simple first-order stepper based on `Euler's method`_
- one using a (simple) Runge-Kutta_ implementation in matplotlib
- and one based on scipy's odeint_ function


.. code-block:: python

    import numpy as np
    from matplotlib import mlab
    from scipy import integrate

    def euler(f, pts, dt):
        vel = np.asarray([f(xy) for xy in pts])
        return pts + vel * dt

    def rk4(f, pts, dt):
        new_pts = [mlab.rk4(f, xy, [0, dt])[-1] for xy in pts]
        return new_pts

    def ode_scipy(f, pts, dt):
        new_pts = [integrate.odeint(f, xy, [0, dt])[-1] for xy in pts]
        return new_pts

    available_integrators = dict(euler=euler, rk4=rk4, scipy=ode_scipy)


These integration functions return updated particle coordinates based on a
velocity function, ``f``; the initial coordinates, ``pts``; and the time step,
``dt``.  These functions would be faster if they operated on all coordinates
simultaneously instead of looping; however, that would require you to join the
(N-by-2) coordinates into a single 1D array so that the integration routines
will run properly. After that, you'd have to split them back up for plotting.

Next, we define a factory function (a function that returns a function) that
connects our integrator to our velocity-field functions. The returned function
will return the next particle position based on the current particle position
and the time step.

.. code-block:: python

    def displace_func_from_velocity_funcs(u_func, v_func, method='rk4'):
        """Return function that calculates particle positions after time step.

        Parameters
        ----------
        u_func, v_func : functions
            Velocity fields which return velocities at arbitrary coordinates.
        method : {'euler' | 'rk4' | 'scipy'}
            Integration method to update particle positions at each time step.
        """

        def velocity(xy, t=0):
            """Return (u, v) velocities for given (x, y) coordinates."""
            # Dummy `t` variable required to work with integrators
            # Must return a list (not a tuple) for scipy's integrate functions.
            return [u_func(*xy), v_func(*xy)]

        odeint = available_integrators[method]

        def displace(xy, dt):
            return odeint(velocity, xy, dt)

        return displace


This function looks long, but it's mostly documentation and comments.


Animations in Matplotlib
========================

Finally, we get to the animation portion. Matplotlib (or more precisely, Ryan
May) added the animation_ module in version 1.1. This module greatly simplifies
the process of generating animations. Nevertheless, I wanted a way to reuse
animations, which didn't seem terribly easy based on the `animation
examples`_.  I ended up creating a fairly simple `Animation class`_, which uses
(but doesn't subclass) matplotlib's animation class.

The following example uses `mpltools.animation` to plot particles in
a potential flow. There are a few important parts:

- ``__init__`` creates a figure (the name ``self.fig`` is required) where the
  animation gets drawn.
- ``init_background`` draws any background elements that aren't updated
  between frames (optional).
- ``update`` adds particles on the left side of the frame, updates their positions
  for a specified time step, and removes particles that leave the right side of
  the frame.


.. code-block:: python

    import matplotlib.pyplot as plt
    from mpltools.animation import Animation
    plt.rc('contour', negative_linestyle='solid')

    class StreamFuncAnim(Animation):

        def __init__(self, stream_function, dt=0.05, xlim=(-1, 1), ylim=None):
            self.dt = dt
            # Initialize velocity field and displace *functions*
            self.u, self.v = velocity_field(stream_function)
            self.displace = displace_func_from_velocity_funcs(self.u, self.v)
            # Save bounds of plot
            self.xlim = xlim
            self.ylim = ylim if ylim is not None else xlim
            # Animation objects must create `fig` and `ax` attributes.
            self.fig, self.ax = plt.subplots()
            self.ax.set_aspect('equal')

        def init_background(self):
            """Draw background with streamlines of flow.

            Note: artists drawn here aren't removed or updated between frames.
            """
            x0, x1 = self.xlim
            y0, y1 = self.ylim
            # Create 100 x 100 grid of coordinates.
            Y, X =  np.mgrid[x0:x1:100j, y0:y1:100j]
            # Horizontal and vertical velocities corresponding to coordinates.
            U = self.u(X, Y)
            V = self.v(X, Y)
            self.ax.streamplot(X, Y, U, V, color='0.7')

        def update(self):
            """Update locations of "particles" in flow on each frame frame."""
            pts = []
            while True:
                pts = list(pts)
                pts.append((self.xlim[0], random_y(self.ylim)))
                pts = self.displace(pts, self.dt)
                pts = np.asarray(pts)
                pts = remove_particles(pts, self.xlim, self.ylim)
                self.ax.lines = []

                x, y = np.asarray(pts).transpose()
                lines, = self.ax.plot(x, y, 'ro')
                yield lines, # return line so that blit works properly


In the ``update`` method, I've chosen to clear and redraw all the displayed
particles, but it would probably be more efficient to update the particle
positions.

``StreamFuncAnim`` calls a couple of small utility functions: First,
``random_y``, which returns a random y-position within the domain so that we
can add particles to the left edge.


.. code-block:: python

    def random_y(ylim):
        yrange = np.diff(ylim)
        return yrange * np.random.rand(1)[0] + ylim[0]


It also calls ``remove_particles``, which removes particles that are outside
the limits of the plot.


.. code-block:: python

    def remove_particles(pts, xlim, ylim):
        if len(pts) == 0:
            return []
        outside_xlim = (pts[:, 0] < xlim[0]) | (pts[:, 0] > xlim[1])
        outside_ylim = (pts[:, 1] < ylim[0]) | (pts[:, 1] > ylim[1])
        keep = ~(outside_xlim|outside_ylim)
        return pts[keep]


Now we have an animation class, ``StreamFuncAnim``, that we can use to animate
the flow of particles.


Particles flowing around a cylinder
===================================

For this example, let's copy a function from a previous article on `stream
functions in potential flow`_. The following function defines the stream
function (in symbolic form) for a cylinder in a uniform flow:


.. code-block:: python

    import sympy
    from sympy.abc import x, y

    radius = 1

    def cylinder_stream_function(U=1, R=radius):
        r = sympy.sqrt(x**2 + y**2)
        psi = U * (r - R**2 / r) * sympy.sin(sympy.atan2(y, x))
        return psi


We could go ahead and use ``StreamFuncAnim`` to animate particles in this flow,
but instead, let's subclass ``StreamFuncAnim`` and add a circle to identify
where the cylinder is defined:


.. code-block:: python

    class CylinderFlow(StreamFuncAnim):
        def init_background(self):
            StreamFuncAnim.init_background(self)
            c = plt.Circle((0, 0), radius=radius, facecolor='none')
            self.ax.add_patch(c)


Finally, we can show this animation by passing an instance of the stream
function to the animation class and calling its ``animate`` method:


.. code-block:: python

    stream_function = cylinder_stream_function()
    cylinder_flow = CylinderFlow(stream_function, xlim=(-3, 3))
    cylinder_flow.animate(blit=True)
    plt.show()


.. raw:: html

   <video controls="controls">
       <source src="images/posts/2012/particles_flowing_around_cylinder.webm" type="video/webm"/>
       <source src="images/posts/2012/particles_flowing_around_cylinder.m4v"/>
       Video display requires browser that supports webm or m4v.
   </video>

Science!


Final thoughts
==============

It's interesting to note that the Euler method is noticeably less-accurate than
``'rk4'`` or scipy's integration routines (as one might expect). Particles
entering and leaving the frame should do so symmetrically (particle paths on
the right of the sphere should mirror those on the left). When using the naive
``'euler'`` implementation, however, noticeable errors build up: Particles
entering along the centerline of the cylinder (i.e. the stagnation point) will
drift away from the centerline by the time they reach the opposite side of the
cylinder.  I haven't noticed much difference between matplotlib's ``'rk4'``
implementation and the more-accurate functions in ``scipy.integrate``, but in
real-world use, scipy's functions are preferred.


.. _stream functions in potential flow:
   http://tonysyu.github.com/plotting-streamlines-with-matplotlib-and-sympy.html

.. _animation:
    http://matplotlib.sourceforge.net/api/animation_api.html

.. _numerical integration:
    http://en.wikipedia.org/wiki/Numerical_ordinary_differential_equations

.. _Euler's method:
    http://en.wikipedia.org/wiki/Euler_method

.. _Runge-Kutta:
    http://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_method

.. _odeint:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html#scipy.integrate.odeint

.. _animation examples:
    http://matplotlib.sourceforge.net/examples/animation/index.html

.. _Animation class:
    https://github.com/tonysyu/mpltools/blob/master/mpltools/animation.py#L27

.. _mpltools.animation:
    http://tonysyu.github.com/mpltools/api/mpltools.animation.html#mpltools.animation.Animation

