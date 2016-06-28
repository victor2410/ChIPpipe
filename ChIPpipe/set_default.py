#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# set_default.py
# ======================
# Author: Gaborit Victor
# Date: Jun 22, 2016
# ======================

"""
  	Functions to setting parameters to default values:

  	- Setting all parameters to default
  	- Get a prefix from a file name
  	- Create default output directory
"""

# Packages required for this programm

import os
import sys
import re
from check import *

def initParamCa(): # Initialize all parameters to default values
	outputdir = os.getcwd()+'/ChIPalign_out'
	selectodir = 'false'
	filterqual = 'OFF'
	unmapped = 'OFF'
	filtercoord = 'OFF'
	indexGenome = 'OFF'
	rmvdup = 'OFF'
	sorting = 'OFF'
	indexBam = 'OFF'
	prefix = str()
	coordiantefile = str()
	genome = str()
	minQ= 0
	fastqfile = str()
	fastqfile1 = str()
	fastqfile2 = str ()
	seq = str()
	return outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, prefix, coordiantefile , genome, minQ, fastqfile, fastqfile1, fastqfile2, seq

def initParamCp(): # Initialize all parameters to default values
	outputdir = os.getcwd()+'/CallPeaks_out'
	selectodir = 'false'
	rep1 = str()
	rep2 = str()
	ctrl1 = str()
	ctrl2 = str ()
	ctrlsup = 'false'
	idr = 'OFF'
	idrthresh = 0
	finalsets = 'OFF'
	plot = 'ON'
	prefix = str()
	return outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix

def initParamCpnr(): # Initialize all parameters to default values
	outputdir = os.getcwd()+'/CallPeaks_norep_out'
	selectodir = 'false'
	bamfile = str()
	ctrlfile = str()
	thresh = '1e-3'
	model = 'ON'
	prefix = str()
	return outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix

def getPrefix(file_in): # Get the prefix name of a specified file when no prefix is given
	m = re.search('[^.]*',file_in)
	return os.path.basename(m.group(0))

def createOdir(directory): # Create an output directory in the current directory when no output directory is given
	if checkPath(directory):
		return
	else:
		os.mkdir(directory)