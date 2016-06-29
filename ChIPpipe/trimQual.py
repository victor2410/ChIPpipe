#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# trimQual.py
# ======================
# Author: Gaborit Victor
# Date: Jun 29, 2016
# ======================

"""
   Main package for trimQual tools, to control quality of fastq file
"""

# packages required for this programm

import os
import sys
from print_message import usageTq, welcomeTq, running, parametersTq, goodbyeCp
from get_opt import readOptTq
from set_default import initParamTq, createOdir, setAdapts
from check import checkRequiredTq
from Callfastqc import fastQc
from Calltrimo import trimmoSe, trimmoPe


def mainTq(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageTq()
		sys.exit(1)
	outputdir, selectodir, fastqfile1, fastqfile2, fastqfile, seq1, seq2, lib = initParamTq()
	outputdir, selectodir, fastqfile1, fastqfile2, fastqfile, seq1, seq2, lib = readOptTq(argv[1:], outputdir, selectodir, fastqfile1, fastqfile2, fastqfile, seq1, seq2, lib)
	checkRequiredTq(fastqfile, fastqfile1, fastqfile2, lib) # check if the required options have been specified
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeTq() # print welcome message
	adaptaters = setAdapts(seq1, seq2, lib)
	parametersTq(outputdir, fastqfile, fastqfile1, fastqfile2, adaptaters, lib, seq1, seq2)
	running() # print running message
	print "Step1 : Quality check before trimming..."
	createOdir(outputdir+"/fastqc_report")
	if fastqfile != '':
		fastQc(fastqfile, outputdir)
	else:
		fastQc(fastqfile1, outputdir)
		fastQc(fastqfile2, outputdir)
	print "Step1 : Quality check before trimming achieved..."
	print ""
	print "Step2 : Trimming..."
	createOdir(outputdir+"/fastq_trim")
	if fastqfile != '':
		fastqtrim = trimmoSe(fastqfile, outputdir, adaptaters)
	else:
		fastqtrim1, fastqtrim2 = trimmoPe(fastqfile1, fastqfile2, outputdir, adaptaters)
	print "Step2 : Trimming achieved..."
	print ""
	print "Step3 : Quality check after trimming..."
	if fastqfile != '':
		fastQc(fastqtrim, outputdir)
	else:
		fastQc(fastqtrim1, outputdir)
		fastQc(fastqtrim2, outputdir)
	print "Step3 : Quality check after trimming achieved..."
	goodbyeCp() # print end of analysis message and the exit
	return