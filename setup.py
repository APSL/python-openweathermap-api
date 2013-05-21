#!/usr/bin/env python

from distutils.core import setup

__version__ = '0.0.1'

setup(name='pyowm',
    version=__version__,
    description='A python wrapper around the Open Weather map api',
    author='Philipp Resch',
    author_email='philipp.resch@bestplaces.at',
    url='https://github.com/APSL/python-openweathermap-api',
    packages=['pyowm', 'pyowm.test'],
    license='GPLv3',
    keywords = 'weather open weather map',
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL 3 License"
    ],
    install_requires=[
            "simplejson>=3.3.0",
    ],
)
