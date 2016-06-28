#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import ChIPpipe
setup(
    name='ChIPpipe',
    version=ChIPpipe.__version__,
    packages=find_packages(),
    author="Victor GABORIT",
    author_email="victor.gaborit2@gmail.com",
    description="Pipeline d'analyse de données de ChIP-seq",
    long_description=open('README.md').read(),
    # install_requires=["bowtie2" , "samtools" , "picard-tools"],
    package_data={'ChIPpipe.Rscript': ['*.r', '*.R']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ],
    entry_points = {
        'console_scripts': [
            'ChIPpipe = ChIPpipe:main',
        ],
    },
    license="WTFPL",
)
