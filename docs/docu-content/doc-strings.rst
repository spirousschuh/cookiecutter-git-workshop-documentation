===========
Doc-Strings
===========

Types of Docstrings
===================

There is different entities that posses docstrings. Take a look at the example
from `Wikipedia <https://en.wikipedia.org/wiki/Docstring#Python>`_:

.. code-block:: python

   """The module's docstring"""

   class MyClass:
       """The class's docstring"""

        def my_method(self):
            """The method's docstring"""
            pass

   def my_function():
       """The function's docstring"""
       pass

Most entities have a docstring. You can check it via ``my_entity.__doc__``.


Detailed Docstring
==================

You can use it to explain the user how to use your function in more detail:

.. code-block:: python

   def addition(arg1, arg2):
       """
       This functions adds the first and the second argument.

       :param arg1: the first summand
       :type arg1:  float
       :param arg2: the second and last summand
       :type arg2:  flaot
       :return:     the sum of both summands
       :rtype:      float
       """
       return arg1 + arg2

Why shall we document the function right in the code?

* documentation is close to the code

   * explanation right at hand
   * once you change the code you can change the docu right at the same place

* We can still include the docstring into our main documentation

Autodoc
=======

When you stick to the convention above to describe the function arguments, what
the function returns as well as the typing, you can use automatically generated
documentation.

First thing you need to do is to change the ``conf.py`` file, to tell Sphinx
that it should use `autodoc`.

Therefore go to ``conf.py`` and append the following string to the *extensions*
list.

.. code-block:: python

   extensions = ['sphinx.ext.autodoc']

Now you can use the autofunction feature by adding the following block to your
documentation.

::

   .. autofunction:: .adding_numbers.addition.addition

Please note that ``adding_numbers.addition.addition`` refers to the function
in the same way you would import it. You can see the result here:

.. autofunction:: adding_numbers.addition.addition

Please note that the convention we used here is the one from *reStructuredText*.
There is other conventions from Google as well as from Numpy that are fairly
common.
