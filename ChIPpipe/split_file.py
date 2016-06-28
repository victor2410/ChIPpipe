#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# split_file.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
	Package called to split file randomly
"""

# Packages required for this programm

from shlex import split
import subprocess
import os
from set_default import getPrefix

def splitFile(file_in, outputdir):
	print ""
	print "splitting file :"+file_in+"..."
	command1 = "gunzip "+file_in # unzip file
	subprocess.call(command1, shell=True)
	unzipname = outputdir+getPrefix(file_in)+".tagAlign"
	prprefix = outputdir+getPrefix(file_in)
	linecount = len(open(unzipname, 'rU').readlines()) # count number of lines in file
	linecount = linecount/2 # get half number of lines
	command2 = "gzip "+unzipname # zip file
	subprocess.call(command2, shell=True)
	command3 = "zcat "+file_in+"|shuf|split -d -l "+str(linecount)+" - "+prprefix # shuffle the file and then split it into two size equal files
	subprocess.call(command3, shell=True)
	command4 = "gzip "+prprefix+"00" # zip the two resulting files
	command5 = "gzip "+prprefix+"01"
	command6 = "mv "+prprefix+"00.gz "+prprefix+"_PR1.tagAlign.gz" # rename the two files
	command7 = "mv "+prprefix+"01.gz "+prprefix+"_PR2.tagAlign.gz"
	subprocess.call(command4, shell=True)
	subprocess.call(command5, shell=True)
	subprocess.call(command6, shell=True)
	subprocess.call(command7, shell=True)
	print file_in+" splitted..."
	return