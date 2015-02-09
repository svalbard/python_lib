#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os.path import dirname, realpath, join
import re


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

# A comment is a line starting with # or --
is_comment = re.compile('^\s*(#|--).*').match


def load_requirements(fname):
    here = dirname(realpath(__file__))
    fname = join(here, fname)

    with open(fname) as fo:
        return [line.strip() for line in fo
                if not is_comment(line) and line.strip()]

setup(
    name='python_lib',
    version='0.1.1',
    description="A stub repository for your next python library",
    long_description=readme + '\n\n' + history,
    author="Svalbard",
    author_email='svalbard@example.com',
    url='https://github.com//python_lib',
    packages=[
        'python_lib',
    ],
    package_dir={'python_lib':
                 'python_lib'},
    include_package_data=True,
    install_requires=load_requirements('requirements.txt'),
    license="BSD",
    zip_safe=False,
    keywords='python_lib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=load_requirements('test-requirements.txt'),
)
