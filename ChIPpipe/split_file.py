#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# split_file.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

# Packages required for this programm
from subprocess import Popen, PIPE
from shlex import split
import subprocess
import os
from set_default import getPrefix

def splitFile(file_in, outputdir):
	print ""
	print "splitting file :"+file_in+"..."
	command1 = "gunzip "+file_in
	subprocess.call(command1, shell=True)
	unzipname = outputdir+getPrefix(file_in)+".tagAlign"
	prprefix = outputdir+getPrefix(file_in)
	linecount = len(open(unzipname, 'rU').readlines())
	linecount = linecount/2
	command2 = "gzip "+unzipname
	subprocess.call(command2, shell=True)
	command3 = "zcat "+file_in+"|shuf|split -d -l "+str(linecount)+" - "+prprefix
	subprocess.call(command3, shell=True)
	command4 = "gzip "+prprefix+"00"
	command5 = "gzip "+prprefix+"01"
	command6 = "mv "+prprefix+"00.gz "+prprefix+"_PR1.tagAlign.gz"
	command7 = "mv "+prprefix+"01.gz "+prprefix+"_PR2.tagAlign.gz"
	subprocess.call(command4, shell=True)
	subprocess.call(command5, shell=True)
	subprocess.call(command6, shell=True)
	subprocess.call(command7, shell=True)
	print file_in+" splitted..."
	return