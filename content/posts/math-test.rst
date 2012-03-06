=========
Math test
=========
:status: draft

Inline math defined using Sphinx role: :math:`\vec{F} = m\vec{a}`.

An equation defined using Sphinx directive:

.. math::

   \nabla^2 \phi = 0

Inline math using the operators defined in the attached script: $a x^2 + b x + c = F(x)$.

An equation on it's own line:

$$ \\frac{\\partial \\rho}{\\partial t} = 0  $$


.. raw:: html

   <script type="text/x-mathjax-config">
   MathJax.Hub.Config({
   extensions: ["tex2jax.js"],
   jax: ["input/TeX", "output/HTML-CSS"],
   tex2jax: {
     inlineMath: [ ['$','$'], ["\\(","\\)"] ],
     displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
     processEscapes: true
   },
   "HTML-CSS": { availableFonts: ["TeX"] }
   });
   </script>
   <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

