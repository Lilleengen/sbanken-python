#!/usr/bin/env python3

from setuptools import setup

setup(
    name='sbanken',
    version='1',
    description='Get bank account information from Sbanken in python',
    long_description=open('README.md').read(),
    author='Henrik Lilleengen',
    author_email='henrik@lilleengen.io',
    url='https://github.com/lilleengen/sbanken',
    download_url = 'https://github.com/lilleengen/sbanken/archive/0.1.tar.gz',
    packages=['sbanken'],
    install_requires=[
        'requests',
    ],
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
    ],
)
