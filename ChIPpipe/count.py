#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# count.py
# ======================
# Author: Gaborit Victor
# Date: Jun 30, 2016
# ======================

"""
	Package to lines in files
"""

# packages required for this programm
import os

def countLines(filein):
	myfile = open(filein, 'r')
	nbline = 0
	lines = myfile.readlines()
	myfile.close()
	for line in lines:
		nbline += 1
	return nbline