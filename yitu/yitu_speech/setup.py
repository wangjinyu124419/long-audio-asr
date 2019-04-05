#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018-Present Shanghai Yitu Technology Co., Ltd. 
# Licensed under the Apache License, Version 2.0

# Yitu SDK
from setuptools import setup, find_packages
from common import constants

with open("README.rst") as fp:
    LONG_DESCRIPTION = fp.read()

setup(
    name = 'yitu-speech-python-sdk',
    version = str(constants.CONSTANT_VERSION),
    packages = find_packages(),
    install_requires=[
        'requests',
    ],
    license = 'Apache License 2.0',
    author = 'Yitu',
    url = 'speech.yitutech.com',
    description = 'Yitu Long speech SDK',
    long_description = LONG_DESCRIPTION,
    keywords = ['yitu', 'sdk', 'speech'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ]
)
