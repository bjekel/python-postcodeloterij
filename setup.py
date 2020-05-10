#!/usr/bin/env python
# -*- coding:utf-8 -*-

import io

from setuptools import setup


version = '0.0.1'


setup(name='python-postcodeloterij',
      version=version,
      description='Python API for talking to Postcode Loterij',
      long_description=io.open('README.rst', encoding='UTF-8').read(),
      keywords='See what prizes were won for a given month and postal code',
      author='Bart Jekel',
      author_email='bartjekel@gmail.com',
      url='https://github.com/bartjekel/python-postcodeloterij/',
      packages=['postcodeloterij'],
      install_requires=['requests>=2.0.0']
      )
