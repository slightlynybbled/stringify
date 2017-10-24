#!/usr/bin/env python

from setuptools import setup, find_packages
import os

__version__ = None

# provide correct path for version
here = os.path.dirname(os.path.dirname(__file__))
exec(open(os.path.join(here, 'stringify/version.py')).read())

# uses the readme.rst as the long description
with open('readme.rst') as f:
    readme = f.read()

# requirements list is pretty short, so there is little
# need for a requirements.txt at the moment
requirements = []

setup(
    name='stringify',
    version=__version__,
    description='Automatic string encoding of'
                'binary files into python variables',
    long_description=readme,
    author='Jason R. Jones',
    author_email='slightlynybbled@gmail.com',
    url='https://github.com/slightlynybbled/stringify',
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    setup_requires=['flake8'],
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
