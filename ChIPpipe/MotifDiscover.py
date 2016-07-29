#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# MotifDiscover.py
# ======================
# Author: Gaborit Victor
# Date: Jul 25, 2016
# ======================

"""
	Package to perform motif discovery analysis related on MEME suite 
"""

# Packages required for this programm

import os
import sys
from print_message import usageMd, welcomeMd, parametersMd, running, goodbyeCp
from set_default import initParamMd, createOdir
from get_opt import readOptMd
from check import checkRequiredMd
from transform import toFastaFile
from motif import motifDeNovo, motifFull


def mainMd(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageMd()
		sys.exit(1)
	outputdir, selectodir, regionfile, genomefile, database, scan, prefix = initParamMd() # intialize to default all parameters
	outputdir, selectodir, regionfile, genomefile, database, scan, prefix = readOptMd(argv[1:], outputdir, selectodir, regionfile, genomefile, database, scan, prefix)
	checkRequiredMd(regionfile, genomefile)
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeMd() # print welcome message
	parametersMd(outputdir, regionfile, genomefile, database, scan, prefix) # print a summary of all parameters used
	running() # print running message
	print ""
	print "Step1: Transforming region bed file to fasta file..."
	fastafile = toFastaFile(regionfile, genomefile, outputdir, prefix)
	print "Step1: Transforming region bed file to fasta file achieved..."
	print ""
	print "Step2: Motif Discovery performed by MEME suite..."
	if scan == 'ON':
		motifFull(fastafile, outputdir, database, prefix)
	else:
		motifDeNovo(fastafile, outputdir, prefix)
	print "Step2: Motif Discovery performed by MEME suite achieved..."
	goodbyeCp()
	return