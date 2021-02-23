#!/usr/bin/env python
import setuptools


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
      name='adding_numbers',
      version='0.0.1',
      description='Git Workshop Documentation',
      author='Christoph Lange',
      author_email='christoph.lange@tu-berlin.de',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      install_requires=[
            'sphinx',
      ],
      python_requires='>=3.6',
)
