#!/usr/bin/env python3
# vi:set fileencoding=utf-8 :

"""
Created on 2014-06-27

@author : Laurent Stacul
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
from darte7 import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='darte7',

    # Versions should comply with PEP440. For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=__version__,

    description='Helper to download documentaries on Arte+7',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/stac47/darte7',

    # Author details
    author='Laurent Stacul',
    author_email='laurent.stacul@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: French',
        'Operating System :: OS Independent',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        # Topics
        'Topic :: Internet',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities',
    ],

    keywords='arte arte+7 video download',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'darte7=darte7.darte7:main',
        ],
    },
)
