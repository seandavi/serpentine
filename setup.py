#!/usr/bin/env python

from distutils.core import setup

setup(name='Serpentine',
      version='0.1.1',
      description='Workflows for bioinformatics based on snakemake',
      author='Sean Davis & Jack Zhu',
      author_email='seandavi@gmail.com',
      url='https://github.com/seandavi/serpentine',
      package_data={'rules': ['rules/*.rules'],
                    'workflows': ['workflows']}
      #scripts=['scripts/*']
     )
