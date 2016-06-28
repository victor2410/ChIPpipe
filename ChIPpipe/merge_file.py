#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# merge_file.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

# Packages required for this programm
from subprocess import Popen, PIPE
from shlex import split
import subprocess

def mergeFile(file1,file2, outputdir, name):
	print "Merging files..."
	outfile=outputdir+name+".tagAlign.gz"
	command = "zcat "+file1+" "+file2+"|gzip -c > "+outfile
	subprocess.call(command, shell=True)
	print "Merging files achieved..."
	return outfile
