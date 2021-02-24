======
Sphinx
======

`Sphinx <https://www.sphinx-doc.org/en/master/>`_ is a tool to build any kind
of documenation.

Why shall we use it?
====================

* converts reStructuredText to an output format, i.e. html
* creates links etc. within and amount documents
* supports many customizations
* native python documentation tool widely adapted

   * `NumPy <https://numpy.org/doc/stable/reference/>`_
   * `SciPy <https://docs.scipy.org/doc/scipy/reference/>`_
   * `scikit-learn <https://scikit-learn.org/stable/>`_

* change documentation via git

Quick Start
===========

If you want to add documenation to a project, please checkout
`this guide <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#quick-start>`_.


Example
=======


Now you can start writing actual documentation. Each html page corresponds
to one ``.rst`` file. So image we want to document a coffee machine.

.. code-block::
   :caption: index.rst
   :name: The landing page of your documentation.

   Congrats for buying our new super awesome coffee-machine. Here we provide
   more details on the following topics.

   .. toctree::
      :maxdepth: 2
      :caption: Table of Content

      safety
      quickstart

This table of content will do three things:

* create links to the heading in ``saftety.rst`` and ``quickstart.rst`` right
    there up to level 2
* create a navigation menu on the side
* tell sphinx that these documents form a joint assemble

To complete the example we have the two missing files linked in the table of
content.

.. code-block::
   :caption: safety.rst
   :name: safety instructions

   Read everything very very carefully.

   Safety
   ======

   This coffee machine can only be installed by an electrician. If you do
   otherwise, you loose all warranty.


   Responsibility (level 1)
   ========================

   We assure you that we don't take any responsibility. Never.

   Exception (level 2)
   ___________________

   No exceptions.

   Exception (level 3)
   *******************

   Really?

So the last heading ``Exception (level 3)`` will not appear in the table of
content of the index page. All other heading will.

.. code-block::
   :caption: quickstart.rst
   :name: quickstart

   Instructions
   ============

   Follow the following steps:

   #. Take the machine out of its box.
   #. PLug the cable into the socket.
   #. Switch it on.




Afterwards please take a look at the ``conf.py`` file. This is the place to go
to when customizing your documentation.