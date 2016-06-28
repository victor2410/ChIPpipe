#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# CallPeaks.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
   Main Package for CallPeaks tools, related on ENCODE IDR protocol
"""

# packages required for this programm

import os
import sys
from print_message import usageCp, welcomeCp, running, goodbyeCp, parametersCp
from set_default import initParamCp, createOdir, getPrefix
from get_opt import readOptCp
from check import checkRequiredCp
from transform import toTagAlign, newName
from merge_file import mergeFile
from split_file import splitFile
from Callspp import peakCall
from IDRanalysis import consistency, countConsistentPeaks
from export import exportResults
from plot import plotResults
from final import createFinalSets

def mainCp(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCp()
		sys.exit(1)
	outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix = initParamCp() # initialize paramters to default
	outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix = readOptCp(argv[1:], outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix) # read option from command line and changes parameters if necessary
	checkRequiredCp(rep1, rep2, ctrl1) # Check if the required parameters have been specified
	if selectodir == 'false': # if no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeCp() # print welcome message
	if prefix ==  '': # if no prefix is given in the command line, give a default prefix
		prefix = 'CallPeaks' 
	parametersCp(outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix) # print a summary off all parameters used
	running() # print running message
	print ""
	print "Step1 : Transformation from bam file to tagAlign file..."
	createOdir(outputdir+"/tagAlignfiles") # create new folder to put transformed files
	for file_in in (rep1, rep2, ctrl1):
		toTagAlign(file_in, outputdir+"/tagAlignfiles/") # convert bam files to tagAlign files
	if ctrlsup == 'true': # if there is a second control file, convert it too
		toTagAlign(ctrl2, outputdir+"/tagAlignfiles/")
		ctrl2 = newName(ctrl2, outputdir+"/tagAlignfiles/") # rename file variables
	rep1 = newName(rep1, outputdir+"/tagAlignfiles/")
	rep2 = newName(rep2, outputdir+"/tagAlignfiles/")
	ctrl1 = newName(ctrl1, outputdir+"/tagAlignfiles/")
	print "Step1 : Transformation from bam file to tagAlign file achieved..."
	print ""
	print "Step2 : Merging Control files (if two files are given)..."
	if ctrlsup == 'true': # if there is two control files , merge them as one
		ctrlfile = mergeFile(ctrl1, ctrl2, outputdir+"/tagAlignfiles/", 'Control')
		print "Step2 : Merging Control files achieved..."
	else:
		print "skipped"
		ctrlfile = ctrl1
	print ""
	print "Step3 : Creating Pool of replicates..."
	poolfile = mergeFile(rep1, rep2, outputdir+"/tagAlignfiles/", 'Pool') # merge two sample files to create pool
	print "Step3 : Creating Pool of replicates achieved..."
	print ""
	print "Step4 : Splitting samples files into pseudo replicates..."
	for file_in in (rep1, rep2, poolfile): # for each file given, split randomly into two pseudo replicates
		splitFile(file_in, outputdir+"/tagAlignfiles/")
	print "Step4 : Splitting samples files into pseudo replicates achieved..."
	print ""
	prefixr1 = getPrefix(rep1)
	prefixr2 = getPrefix(rep2)
	prefixpool = getPrefix(poolfile)
	prefixr1 = outputdir+"/tagAlignfiles/"+prefixr1
	prefixr2 = outputdir+"/tagAlignfiles/"+prefixr2
	prefixpool = outputdir+"/tagAlignfiles/"+prefixpool
	print "Step5 : Peak Calling for each files (replicates, pool and pseudo replicates)..."
	createOdir(outputdir+"/PeakCalling") # create new folder to put peak calling output
	for i in (rep1, rep2, poolfile, prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz"):
		peakCall(i, ctrlfile, outputdir+"/PeakCalling/") # for each files given, perform peak calling with spp
	print "Step5 : Peak Calling for each files achieved..."
	print ""
	print "Step6 : IDR analysis..."
	if idr == 'OFF':
		print "Skipped"
	else: # if idr analysis is selected 
		createOdir(outputdir+"/IDR") # create new folder to put IDR output, then, perform IDR analysis between each replicates and each pseudo-replicates
		consistency(rep1, rep2, ctrlfile, outputdir) 
		consistency(prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		consistency(prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		consistency(prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		nt = countConsistentPeaks(rep1, rep2, outputdir, idrthresh) # get number of peaks with IDR lower than specified threshold for each IDR output file
		np = countConsistentPeaks(prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz", outputdir, idrthresh)
		n1 = countConsistentPeaks(prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", outputdir , idrthresh)
		n2 = countConsistentPeaks(prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", outputdir , idrthresh)
		exportResults(nt, np, n1, n2, outputdir) # export metrics in a tab delimited file
		print "Step6 : IDR analysis achieved..."
	print ""
	print "Step7 : Plotting IDR results..."
	if plot == 'OFF':
		print "Skipped"
	else: # if no-plot option is not selected
		createOdir(outputdir+"/IDR/plots") # create new folder to put IDR plot, then, create the plots for each IDR output files
		plotResults(outputdir, rep1, rep2, prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz")
		print "Step7 : Plotting IDR results achieved..."
	print ""
	print "Step8 : Creating final sets of peaks..."
	if finalsets == 'OFF':
		print "Skipped"
	else: # if final peak sets creation is asked
		createOdir(outputdir+"/finalsets")  # create new folder to put final peak sets, then, create final peak sets
		createFinalSets(poolfile , ctrlfile, nt, np, outputdir, prefix)
		print "Step8 : Creating final sets of peaks achieved..."
	goodbyeCp() # print end message and then exit
	return