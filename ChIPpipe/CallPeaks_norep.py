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
from Callspp import estimateParam
from Callmacs import peakCallMacs1, peakCallMacs2

def mainCpnr(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCpnr()
		sys.exit(1)
	outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix = initParamCpnr() # intialize to default all parameters
	outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix  = readOptCpnr(argv[1:], outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix ) # read option on command line and changes parameters if necessary
	checkRequiredCpnr(bamfile, ctrlfile) # check if the required options have been specified
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeCpnr() # print welcome message
	if prefix ==  '': # If no prefix is given in the command line, give a default prefix
		prefix = 'CallPeaks_norep'
	parametersCpnr(outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix) # print a summary of all parameters used
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
	print "Step2 : Estimating PeakCalling parameters by phantomPeaksQualTools..."
	createOdir(outputdir+"/PeakCalling")
	if model != 'ON': # if no-model options have been used, the parameters for peak calling have to be estimate by spp
		fragmentsize, halffrag = estimateParam(chipfile, outputdir+"/PeakCalling", prefix)
		print "Step2 : Estimating PeakCalling parameters by phantomPeaksQualTools achieved..."
		print ""
	else:
		print "skipped"
		print ""
	print "Step3 : PeakCalling using macs2..." 
	if model != 'ON': # peak calling with macs depending on the model
		peakCallMacs1(chipfile, ctrlfile, outputdir+"/PeakCalling/", prefix, thresh, halffrag, fragmentsize)
	else:
		peakCallMacs2(chipfile, ctrlfile, outputdir, prefix, thresh)
	print "Step3 : PeakCalling using macs2 achieved..."
	goodbyeCp() # print end of analysis message and the exit
	return


