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
from set_default import initParamCpnr, createOdir, getPrefix
from get_opt import readOptCpnr
from check import checkRequiredCpnr
from transform import toTagAlign, newName
from Callspp import qualCheck, peakCall
from Callmacs import  peakCallMacs
from split_file import splitFile
from IDRanalysis import consistency, countConsistentPeaks
from plot import plotResults2
from final import createFinalSets2

def mainCpnr(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCpnr()
		sys.exit(1)
	outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix, spp = initParamCpnr() # intialize to default all parameters
	outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix, spp  = readOptCpnr(argv[1:], outputdir, selectodir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix, spp ) # read option on command line and changes parameters if necessary
	checkRequiredCpnr(bamfile, ctrlfile) # check if the required options have been specified
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeCpnr() # print welcome message
	if prefix ==  '': # If no prefix is given in the command line, give a default prefix
		prefix = 'CallPeaks_norep'
	parametersCpnr(outputdir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix, spp) # print a summary of all parameters used
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
	if qc == 'ON' and spp == 'OFF': # Cross-correlation analysis is asked
		qualCheck(chipfile, outputdir+"/PeakCalling", prefix)
		print "Step2 : Cross-correlation by phantomPeaksQualTools before calling peaks..."
		print ""
	else:
		print "skipped"
		print ""
	print "Step3 : PeakCalling using macs2..." 
	if spp == 'OFF':
		peakCallMacs(chipfile, ctrlfile, outputdir, prefix, pvalue, qvalue, thresh)
		print "Step3 : PeakCalling using macs2 achieved..."
		print ""
	else:
		print "skipped"
		print ""
	if spp == 'ON':
		print "Step4 : PeakCalling based on adaptated IDR analysis..."
		print "\tStep4a : Splitting file into pseudo-replicates..."
		splitFile(chipfile, outputdir+"/tagAlignfiles/")
		print "\tStep4a : Splitting file into pseudo-replicates achieved..."
		prefixchip = getPrefix(chipfile)
		prefixchip = outputdir+"/tagAlignfiles/"+prefixchip
		print "Step4b : Peak Calling for each files (replicates and pseudo replicates)..."
		createOdir(outputdir+"/PeakCalling") # create new folder to put peak calling output
		for i in (chipfile, prefixchip+"_PR1.tagAlign.gz", prefixchip+"_PR2.tagAlign.gz"):
			peakCall(i, ctrlfile, outputdir+"/PeakCalling/") # for each files given, perform peak calling with spp
		print "Step4b : Peak Calling for each files (replicates and pseudo replicates) achieved..."
		print "Step4c : IDR analysis..."
		createOdir(outputdir+"/IDR") # create new folder to put IDR output, then, perform IDR analysis between each replicates and each pseudo-replicates
		consistency(prefixchip+"_PR1.tagAlign.gz", prefixchip+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		idrthresh = 0.01
		np = countConsistentPeaks(prefixchip+"_PR1.tagAlign.gz", prefixchip+"_PR2.tagAlign.gz", outputdir, idrthresh)
		print "number of consistent peaks between the two pseudo replicates: "+str(np)
		print "Step4c : IDR analysis achieved..."
		print "Step4d : Plotting IDR results..."
		createOdir(outputdir+"/IDR/plots") # create new folder to put IDR plot, then, create the plots for each IDR output files
		plotResults2(outputdir, prefixchip+"_PR1.tagAlign.gz", prefixchip+"_PR2.tagAlign.gz")
		print "Step4d : Plotting IDR results achieved..."
		print "Step5e : Creating final sets of peaks..."
		createOdir(outputdir+"/finalsets")  # create new folder to put final peak sets, then, create final peak sets
		createFinalSets2(chipfile , ctrlfile, np, outputdir, prefix)
	goodbyeCp() # print end of analysis message and the exit
	return


