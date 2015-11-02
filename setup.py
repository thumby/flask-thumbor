#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of flask-thumbor.
# https://github.com/thumby/flask-thumbor

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Thumby <dev@thumby.io>

from setuptools import setup, find_packages
from flask_thumbor import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='flask-thumbor',
    version=__version__,
    description='Flask utilities to use thumbor images. ',
    long_description='''
Flask utilities to use thumbor images. 
''',
    keywords='flask python thumbor images responsive',
    author='Thumby',
    author_email='dev@thumby.io',
    url='https://github.com/thumby/flask-thumbor',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'flask-thumbor=flask_thumbor.cli:main',
        ],
    },
)
