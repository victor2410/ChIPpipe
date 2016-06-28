#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# get_opt.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
    Functions calling for getting options parameters:
"""

# Packages required for this programm

import os
import sys
import getopt
from check import *
from print_message import *

# Read options
def readOptCa(argv, outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinatefile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq):
	__version__ = "0.0.1"
	try:                                
	    opts, args = getopt.getopt(argv, "hf:1:2:g:o:q:FL:", ["help", "index", "rmdup", "sort", "bamIndex", "version", "name="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageCa()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageCa()
			sys.exit()
		elif opt == '-f': # Means that just one SE fastq file is given
			checkFastq(arg)
			fastqfile = arg
			seq = 'SE'
		elif opt == '-1': # Means that R1 PE fastq file is given
			checkFastq(arg)
			fastqfile1 = arg
			seq = 'PE'
		elif opt == '-2': # Means that R2 PE fastq file is given
			checkFastq(arg)
			fastqfile2 = arg
		elif opt == '-g': # genome prefix is given
			checkGenome(arg)
			genome = arg
		elif opt == '-o': # Output directory is specified
			if not checkPath(arg):
				print "Error, the specified path '"+arg+"' does not exists"
				sys.exit(1)
			outputdir = arg
			selectodir = 'true'
		elif opt == '-q': # Filter out reads with low quality
			minqual = arg # quality threshold
			filterqual = 'ON'
		elif opt == '-F': # Filter out unmapped reads
			unmapped = 'ON'
		elif opt == '-L': # Filter out reads in specific regions (blacklist)
			checkFile(arg) 
			coordinatefile = arg # file name of blacklist regions
			filtercoord = 'ON'
		elif opt == '--index': # Indexing genome before alignment
			indexGenome = 'ON'
		elif opt == '--rmdup': # Filter out PCR duplicates and non uniquely mappable reads 
			rmvdup = 'ON'
		elif opt == '--sort': # Sorting final bam file
			sorting = 'ON'
		elif opt == '--bamIndex': # Indexing final bam file
			indexBam = 'ON'
		elif opt == '--name': # Prefix to give to output file
			prefix = arg
		elif opt == '--version': # Print software version
			print "ChIPalign."+__version__
			sys.exit(0)
	return outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinatefile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq

def readOptCp(argv, outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix):
	__version__ = "0.0.1"
	try:                                
	    opts, args = getopt.getopt(argv, "h1:2:o:", ["help", "c1=", "c2=", "idr=", "sets", "no-plots", "name=", "version"]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageCp()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageCp()
			sys.exit()
		elif opt == '-1': # For replicate 1 file
			checkBam(arg)
			rep1 = arg
		elif opt == '-2': # For replicate 2 file
			checkBam(arg)
			rep2 = arg
		elif opt == '-o': # Output directory is specified
			if not checkPath(arg):
				print "Error, the specified path '"+arg+"' does not exists"
				sys.exit(1)
			outputdir = arg
			selectodir = 'true'
		elif opt == '--c1': # For control file
			checkBam(arg)
			ctrl1 = arg
		elif opt == '--c2': # For supplemental control file
			checkBam(arg)
			ctrl2 = arg
			ctrlsup = 'true'
		elif opt == '--idr': # Perform IDR analysis
			idr = 'ON'
			idrthresh = arg
		elif opt == '--sets': # Create final peak sets
			finalsets = 'ON'
		elif opt == '--no-plots': # Create final peak sets
			plot = 'OFF'
		elif opt == '--name': # Prefix to give to output file
			prefix = arg
		elif opt == '--version': # Print software version
			print "CallPeaks."+__version__
			sys.exit(0)
	return outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix

def readOptCpnr(argv, outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix ):
	try:                                
	    opts, args = getopt.getopt(argv, "hf:c:o:", ["help", "thresh=", "no-model", "name="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageCpnr()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageCpnr()
			sys.exit()
		elif opt == '-f': # For replicate 1 file
			checkBam(arg)
			bamfile = arg
		elif opt == '-c': # For replicate 2 file
			checkBam(arg)
			ctrlfile = arg
		elif opt == '-o': # Output directory is specified
			if not checkPath(arg):
				print "Error, the specified path '"+arg+"' does not exists"
				sys.exit(1)
			outputdir = arg
			selectodir = 'true'
		elif opt == '--thresh': # Perform IDR analysis
			thresh = arg
		elif opt == '--no-model': # Create final peak sets
			model = 'OFF'
		elif opt == '--name': # Prefix to give to output file
			prefix = arg
	return  outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix

def readOpt(argv):
	__version__ = "0.0.1"
	try:                                
	    opts, args = getopt.getopt(argv, "h", ["help", "version"]) # List of all short and long options possible
	except getopt.GetoptError:
	    usage()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usage()
			sys.exit()
		elif opt == '--version': # Print software version
			print "ChIPpipe."+__version__
			sys.exit(0)
	return
