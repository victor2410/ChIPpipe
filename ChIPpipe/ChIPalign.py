#!/usr/bin/python3.4
# -*-coding:utf-8 -*


# ChIPalign.py
# ======================
# Author: Gaborit Victor
# Date: Jun 21, 2016
# ======================

"""
   Main package for ChIPalign tools
"""

# packages required for this programm

import os
import sys
import getopt
from print_message import usageCa, parametersSe, parametersPe, welcomeCa, running, goodbyeCa
from set_default import initParamCa, createOdir
from get_opt import readOptCa
from check import checkRequiredCa
from Bowtie import genomeIndex, readsAlignment
from filter_reads import unmappedFilter, minQFilter, removeDup, coordFilter
from sorting import sortAndIndexFile

def mainCa(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCa()
		sys.exit(1)
	# Settings default parameters
	outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinateFile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq = initParamCa()      
	# Getting options from command line and changes, if necessary, default parameters
	outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinateFile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq = readOptCa(argv[1:], outputdir, selectodir, filterqual, unmapped, filtercoord, indexGenome, rmvdup, sorting, indexBam, coordinateFile, prefix, genome, minqual, fastqfile, fastqfile1, fastqfile2, seq)
	checkRequiredCa(seq, fastqfile2, genome) # Check if the required options have been specified
	if selectodir == 'false': # If no output directory specified, create one in current directory
		createOdir(outputdir)
	welcomeCa() # Print welcome message to stdout
	if seq == 'SE': # Print all specified parameters following if the data are single-end or paired-end to stdout
		if prefix ==  "": # If no prefix is given in the command line, take the prefixe of fastq file
			prefix = getPrefix(fastqfile) 
		parametersSe(fastqfile, genome, outputdir, filterqual, minqual, unmapped, filtercoord, coordinateFile, indexGenome, rmvdup, sorting, indexBam, prefix)
	else:
		if prefix ==  "":
			prefix = getPrefix(fastqfile1)
		parametersPe(fastqfile1, fastqfile2, genome, outputdir, filterqual, minqual, unmapped, filtercoord, coordinateFile, indexGenome, rmvdup, sorting, indexBam, prefix)
	running() # Print message for starting analysis
	# Calling differents functions to perform the analysis
	genomeIndex(indexGenome, genome)
	bamname = readsAlignment(seq, fastqfile, fastqfile1, fastqfile2, outputdir, genome, prefix) 
	bamname = unmappedFilter(unmapped, outputdir, bamname, prefix) 
	bamname = minQFilter(filterqual, minqual, outputdir, bamname, prefix)
	bamname = removeDup(rmvdup, outputdir, bamname, prefix)
	bamname = coordFilter(filtercoord, coordinateFile, outputdir, bamname, prefix)
	bamname = sortAndIndexFile(sorting, indexBam, outputdir, bamname, prefix)
	goodbyeCa(bamname) # Print to stdout final message and resume the analyze
	return
