=====================================
Task 2: Creating Sphinx Documentation
=====================================

Please create a seperate branch for each of the sub-tasks and create a
Merge Request every time.
You can find detailed instructions on the :ref:`git-workflow` page.


Setup Sphinx
============

Please follow `this guide <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#quick-start>`_
in order to create a basic documentation.


Landing Page
============

Now we want to replace the content of ``index.rst`` with what we already
used for the ``Readme.rst``.

You can quickly build your documentation locally to check if everything is
rendered accordingly.

.. code-block:: bash

   cd /your/project/docs
   make html

   # open the html site in a browser of your choice
   firefox _build/html/index.html

