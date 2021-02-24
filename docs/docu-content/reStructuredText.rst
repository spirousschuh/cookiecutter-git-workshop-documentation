RestructuredText
================

The standard file format that is used in python to write technical
documentation is RestructuredText.

Example
-------

In *RestructuredText* what you type is not what you get. For instance the
following snippet

::

   Features
   ________

   #. Be awesome
   #. Make things faster

   Installation
   ____________

   Install **my_project** by running:

   .. code-block::

      pip install my_project

is rendered to look like the following:

Features
________

#. Be awesome
#. Make things faster

Installation
____________

Install **my_project** by running:

.. code-block::

   pip install my_project


Editing a document is not as straight forward as standard Word Processors, like
Libre Office. The idea of using it for documentation is:


Idea
----

Here some good features of *reStructuredText*:

* automatic formatting
* changes are traceable with git
* auto generated content, i.e. table of content, links
* Speed up writing documentation (once you are familiar with RestructuredText)

Properties
----------

And some things to keep in mind when writing your documentation

* indention is important
* blank lines are very important
* 3 spaces vs. 4 spaces in python
* supports

   * highlighting
   * lists
   * table
   * all sorts of blocks
   * images
   * hyperlinks
   * citations
   * footnotes
   * much more

* can create multiple output formats

   * html
   * LaTEX (pdf)
   * ePub
   * manual pages
   * plain text



For a more detailed introduction on RestructuredText, please take a look at
this `documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.





