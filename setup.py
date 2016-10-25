#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# setup.py


from setuptools import setup

DESCRIPTION = "See ./README.md"
LONG_DESCRIPTION = DESCRIPTION


setup(
    author="Dan'",
    author_email="dan@home",
    name="mfm",
    version="0.0.0",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="http://mfm.dan.net",
    platforms=['OS Independant'],
    license='See ./LICENSE',
    classifiers=[
        "Programming Language::Python::3.5",
    ],
    packages=['src']
)
