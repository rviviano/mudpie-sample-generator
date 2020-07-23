#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mudipie-sample-generator',
      version='0.1.1',
      description='Extract random samples from wav file and save them.',
      author='Raymond Viviano',
      author_email='rayviviano@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      entry_points = { 
            'console_scripts': [ 
                'mudsampgen = mudpie_sample_generator:main'
            ] 
        }, 
      license='LICENSE.md',
    )
