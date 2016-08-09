#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# set_default.py
# ======================
# Author: Gaborit Victor
# Date: Jun 22, 2016
# ======================

"""
  	Package to setting parameters to default values:

  	- Setting all parameters to default
  	- Get a prefix from a file name
  	- Create default output directory
"""

# packages required for this programm

import os
import sys
import re
from check import checkPath

def initParamTq():
	outputdir = os.getcwd()+'/trimQual_out'
	selectodir = 'false'
	fastqfile1 = str()
	fastqfile2 = str()
	fastqfile = str()
	seq1 = str()
	seq2 = str()
	lib = 2
	return outputdir, selectodir, fastqfile1, fastqfile2, fastqfile, seq1, seq2, lib

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
	qc = 'OFF'
	prefix = str()
	pvalue = 'ON'
	qvalue = 'OFF'
	spp = 'OFF'
	return outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix, spp

def initParamAp():
	outputdir = os.getcwd()+'/AnnoPeaks_out'
	selectodir = 'false'
	peakfile = str()
	annofile = str()
	prefix = str()
	peakcaller = str()
	graph = 'OFF'
	return outputdir, selectodir, peakfile, annofile, peakcaller, prefix, graph 

def initParamMd():
	outputdir = os.getcwd()+'/MotifDiscover_out'
	selectodir = 'false'
	regionfile = str()
	genomefile = str()
	database = str()
	scan = 'OFF'
	prefix = 'MotifDiscover'
	return outputdir, selectodir, regionfile, genomefile, database, scan, prefix

def initParamSm():
	outputdir = os.getcwd()+'/ScanMotif_out'
	selectodir = 'false'
	regionfile = str()
	genomefile = str()
	motiffile = str()
	prefix = 'ScanMotif'
	exclude = 'NONE'
	return outputdir, selectodir, regionfile, genomefile, motiffile, exclude, prefix

def getPrefix(file_in): # Get the prefix name of a specified file when no prefix is given
	m = re.search('[^.]*',file_in)
	return os.path.basename(m.group(0))

def createOdir(directory): # Create an output directory in the current directory when no output directory is given
	if checkPath(directory):
		return
	else:
		os.mkdir(directory)

def setAdapts(seq1, seq2, lib):
	if int(lib) == 0:
		if seq2 == '':
			adaptaters="TruSeq2-"+seq1+".fa"
		else:
			adaptaters="TruSeq2-"+seq2+".fa"
	else:
		if seq2 == '':
			adaptaters="TruSeq2-"+seq1+".fa"
		else:
			adaptaters="TruSeq2-"+seq2+".fa"
	return adaptaters