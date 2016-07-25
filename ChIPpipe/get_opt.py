#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# get_opt.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
    package calling for getting options parameters:
"""

# packages required for this programm

import os
import sys
import getopt
from check import checkFastq, checkBam, checkPath, checkGenome, checkFile, checkLib, checkBed
from print_message import usageCa, usageCp, usageCpnr, usage, usageTq, usageAp

def readOptTq(argv, outputdir, selectodir, fastqfile1, fastqfile2, fastqfile, seq1, seq2, lib):
	try:                                
	    opts, args = getopt.getopt(argv, "hf:1:2:o:", ["help", "lib=", "adapt="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageTq()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageTq()
			sys.exit(0)
		elif opt == '-f': # for SE fastq file
			checkFastq(arg)
			fastqfile = arg
			seq1 = 'SE'
		elif opt == '-1': # For R1 fastq file
			checkFastq(arg)
			fastqfile1 = arg
			seq1 = 'PE'
		elif opt == '-2': # For R2 fastq file
			checkFastq(arg)
			fastqfile2 = arg
		elif opt == '-o': # Output directory is specified
			if not checkPath(arg):
				print "Error, the specified path '"+arg+"' does not exists"
				sys.exit(1)
			outputdir = arg
			selectodir = 'true'
		elif opt == '--lib': # For control file
			checkLib(arg)
			lib = arg
		elif opt == '--adapt': # For supplemental control file
			if arg != 'SE' and arg != 'PE':
				print "Error, wrong parameter used for --adapt options, must be 'SE' or 'PE'"
				sys.exit(1)
			seq2 = arg
	return outputdir, selectodir, fastqfile1, fastqfile2, fastqfile, seq1, seq2, lib

# Read options
def readOptCa(argv, outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinatefile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq):
	try:                                
	    opts, args = getopt.getopt(argv, "hf:1:2:g:o:q:FL:", ["help", "index", "rmdup", "sort", "bamIndex", "name="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageCa()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageCa()
			sys.exit(0)
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
	return outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinatefile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq

def readOptCp(argv, outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix):
	try:                                
	    opts, args = getopt.getopt(argv, "h1:2:o:", ["help", "c1=", "c2=", "idr=", "sets", "no-plots", "name="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageCp()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageCp()
			sys.exit(0)
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
	return outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix

def readOptCpnr(argv, outputdir, selectodir, bamfile, ctrlfile, thresh, qc, prefix ):
	try:                                
	    opts, args = getopt.getopt(argv, "hf:c:o:", ["help", "thresh=", "spp-qual", "name="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageCpnr()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageCpnr()
			sys.exit(0)
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
		elif opt == '--spp-qual': # Create final peak sets
			qc = 'ON'
		elif opt == '--name': # Prefix to give to output file
			prefix = arg
	return  outputdir, selectodir, bamfile, ctrlfile, thresh, qc, prefix

def readOptAp(argv,  outputdir, selectodir, peakfile, annofile, peakcaller, prefix, graph):
	try:                                
	    opts, args = getopt.getopt(argv, "hf:a:o:", ["help", "plot", "name="]) # List of all short and long options possible
	except getopt.GetoptError:
	    usageAp()
	    sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"): # Print usage message
			usageAp()
			sys.exit(0)
		elif opt == '-f': # For replicate 1 file
			checkFile(arg)
			peakfile = arg
		elif opt == '-a': # For replicate 2 file
			checkBed(arg)
			annofile = arg
		elif opt == '-o': # Output directory is specified
			if not checkPath(arg):
				print "Error, the specified path '"+arg+"' does not exists"
				sys.exit(1)
			outputdir = arg
			selectodir = 'true'
		elif opt == '--name': # Prefix to give to output file
			prefix = arg
		elif opt == '--plot':
			graph = 'ON'
	return   outputdir, selectodir, peakfile, annofile, peakcaller, prefix, graph

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
			sys.exit(0)
		elif opt == '--version': # Print software version
			print "ChIPpipe."+__version__
			sys.exit(0)
	return
