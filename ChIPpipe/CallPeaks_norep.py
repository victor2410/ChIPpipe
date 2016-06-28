#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# CallPeaks_norep.py
# ======================
# Author: Gaborit Victor
# Date: Jun 27, 2016
# ======================

"""
   Main function for CallPeaks tools, when no biological replicates are available
"""

# Packages required for this programm

import os
import sys
from print_message import *
from set_default import *
from get_opt import *
from check import *
from transform import *
from Callspp import *
from Callmacs import *

def mainCpnr(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCpnr()
		sys.exit(1)
	outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix = initParamCpnr()
	outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix  = readOptCpnr(argv[1:], outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix )
	checkRequiredCpnr(bamfile, ctrlfile)
	if selectodir == 'false': # If no output directory specified, create one in current directory
		createOdir(outputdir)
	welcomeCpnr()
	if prefix ==  '': # If no prefix is given in the command line, give a default prefix
		prefix = 'CallPeaks_norep'
	parametersCpnr(outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix)
	running()
	print ""
	print "Step1 : Transformation from bam file to tagAlign file..."
	createOdir(outputdir+"/tagAlignfiles")
	for file_in in (bamfile, ctrlfile):
		toTagAlign(file_in, outputdir+"/tagAlignfiles/")
	chipfile = newName(bamfile, outputdir+"/tagAlignfiles/")
	ctrlfile = newName(ctrlfile, outputdir+"/tagAlignfiles/")
	print "Step1 : Transformation from bam file to tagAlign file achieved..."
	print ""
	print "Step2 : Estimating PeakCalling parameters by phantomPeaksQualTools..."
	createOdir(outputdir+"/PeakCalling")
	if model != 'ON':
		fragmentsize, halffrag = estimateParam(chipfile, outputdir+"/PeakCalling", prefix)
		print "Step2 : Estimating PeakCalling parameters by phantomPeaksQualTools achieved..."
		print ""
	else:
		print "skipped"
		print ""
	print "Step3 : PeakCalling using macs2..."
	if model != 'ON':
		peakCallMacs1(chipfile, ctrlfile, outputdir+"/PeakCalling/", prefix, thresh, halffrag, fragmentsize)
	else:
		peakCallMacs2(chipfile, ctrlfile, outputdir, prefix, thresh)
	print "Step3 : PeakCalling using macs2 achieved..."
	goodbyeCp()
	sys.exit(0)


