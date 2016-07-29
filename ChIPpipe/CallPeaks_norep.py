#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# CallPeaks_norep.py
# ======================
# Author: Gaborit Victor
# Date: Jun 27, 2016
# ======================

"""
   Main package for CallPeaks tools, when no biological replicates are available
"""

# packages required for this programm

import os
import sys
from print_message import usageCpnr, parametersCpnr, welcomeCpnr, running, goodbyeCp
from set_default import initParamCpnr, createOdir
from get_opt import readOptCpnr
from check import checkRequiredCpnr
from transform import toTagAlign, newName
from Callspp import qualCheck
from Callmacs import  peakCallMacs

def mainCpnr(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCpnr()
		sys.exit(1)
	outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix = initParamCpnr() # intialize to default all parameters
	outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix  = readOptCpnr(argv[1:], outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix ) # read option on command line and changes parameters if necessary
	checkRequiredCpnr(bamfile, ctrlfile) # check if the required options have been specified
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeCpnr() # print welcome message
	if prefix ==  '': # If no prefix is given in the command line, give a default prefix
		prefix = 'CallPeaks_norep'
	parametersCpnr(outputdir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix) # print a summary of all parameters used
	running() # print running message
	print ""
	print "Step1 : Transformation from bam file to tagAlign file..."
	createOdir(outputdir+"/tagAlignfiles") # create new folder to put all tagAlign files
	for file_in in (bamfile, ctrlfile): # convert all given files from bam to tagAlign
		toTagAlign(file_in, outputdir+"/tagAlignfiles/")
	chipfile = newName(bamfile, outputdir+"/tagAlignfiles/") # rename the files
	ctrlfile = newName(ctrlfile, outputdir+"/tagAlignfiles/")
	print "Step1 : Transformation from bam file to tagAlign file achieved..."
	print ""
	print "Step2 : Cross-correlation by phantomPeaksQualTools before calling peaks..."
	createOdir(outputdir+"/PeakCalling")
	if qc == 'ON': # Cross-correlation analysis is asked
		qualCheck(chipfile, outputdir+"/PeakCalling", prefix)
		print "Step2 : Cross-correlation by phantomPeaksQualTools before calling peaks..."
		print ""
	else:
		print "skipped"
		print ""
	print "Step3 : PeakCalling using macs2..." 
	peakCallMacs(chipfile, ctrlfile, outputdir, prefix, pvalue, qvalue, thresh)
	print "Step3 : PeakCalling using macs2 achieved..."
	goodbyeCp() # print end of analysis message and the exit
	return


