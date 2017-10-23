#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open
from setuptools import setup

setup(
    name='jyutping',
    version='0.3.2',
    packages=['jyutping',],
    license='MIT',
    author='Ivor Zhou',
    author_email='hello@ivorz.com',
    url='https://github.com/imdreamrunner/python-jyutping',
    description='Python tool to convert Chinese characters to Jyutping.',
    long_description=open('README.rst', encoding='utf-8').read(),
    include_package_data=True,
)
