#!/usr/bin/env python

from setuptools import setup

setup(name='haste_image_analysis',
      version='0.10',
      packages=['haste_processing_node',
                'haste_processing_node.image_analysis'],
      install_requires=[
          'numpy',
          'Pillow',
          'scikit-image'
          # HarmonicIO_PE -- (not on PyPI)

      ],
      test_requires=[
          'pytest'
      ]
      )
