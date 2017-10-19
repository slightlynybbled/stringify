#!/usr/bin/env python

from setuptools import setup, find_packages
import os


# provide correct path for version
here = os.path.dirname(os.path.dirname(__file__))
exec(open(os.path.join(here, 'stringify/version.py')).read())

requirements = []

setup(
    name='stringify',
    version=__version__,
    description='Automatic string encoding of binary files into python variables',
    author='Jason R. Jones',
    author_email='slightlynybbled@gmail.com',
    url='https://github.com/slightlynybbled/stringify',
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ],
    keywords='string base64 binary'
)

