from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import romanize

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md', 'CHANGES.md')

setup(
    name='Romanize',
    version=romanize.__version__,
    url='https://github.com/gschizas/RomanizePython',
    license='Apache Software License',
    author='George Schizas',
    author_email='gschizas@gmail.com',
    description='Transcribe Greek text to Latin alphabet using the ISO 843:1997 standard (also known as ELOT 743:1987)',
    long_description=long_description,
    packages=['romanize'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Natural Language :: Greek',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing'
    ],
    test_suite="tests", requires=['colorama']
)