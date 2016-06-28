#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# CallPeaks.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
   Main function for CallPeaks tools, related on ENCODE IDR protocol
"""

# Packages required for this programm

import os
import sys
from print_message import *
from set_default import *
from get_opt import *
from check import *
from transform import *
from merge_file import *
from split_file import *
from Callspp import *
from IDRanalysis import *
from export import *
from plot import *
from final import *

def mainCp(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageCp()
		sys.exit(1)
	outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix = initParamCp()
	outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix = readOptCp(argv[1:], outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix)
	checkRequiredCp(rep1, rep2, ctrl1)
	if selectodir == 'false': # If no output directory specified, create one in current directory
		createOdir(outputdir)
	welcomeCp()
	if prefix ==  '': # If no prefix is given in the command line, give a default prefix
		prefix = 'CallPeaks' 
	parametersCp(outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix)
	running()
	print ""
	print "Step1 : Transformation from bam file to tagAlign file..."
	createOdir(outputdir+"/tagAlignfiles")
	for file_in in (rep1, rep2, ctrl1):
		toTagAlign(file_in, outputdir+"/tagAlignfiles/")
	if ctrlsup == 'true':
		toTagAlign(ctrl2, outputdir+"/tagAlignfiles/")
		ctrl2 = newName(ctrl2, outputdir+"/tagAlignfiles/")
	rep1 = newName(rep1, outputdir+"/tagAlignfiles/")
	rep2 = newName(rep2, outputdir+"/tagAlignfiles/")
	ctrl1 = newName(ctrl1, outputdir+"/tagAlignfiles/")
	print "Step1 : Transformation from bam file to tagAlign file achieved..."
	print ""
	print "Step2 : Merging Control files (if two files are given)..."
	if ctrlsup == 'true':
		ctrlfile = mergeFile(ctrl1, ctrl2, outputdir+"/tagAlignfiles/", 'Control')
		print "Step2 : Merging Control files achieved..."
	else:
		print "skipped"
		ctrlfile = ctrl1
	print ""
	print "Step3 : Creating Pool of replicates..."
	poolfile = mergeFile(rep1, rep2, outputdir+"/tagAlignfiles/", 'Pool')
	print "Step3 : Creating Pool of replicates achieved..."
	print ""
	print "Step4 : Splitting samples files into pseudo replicates..."
	for file_in in (rep1, rep2, poolfile):
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
	createOdir(outputdir+"/PeakCalling")
	#for i in (rep1, rep2, poolfile, prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz"):
		#peakCall(i, ctrlfile, outputdir+"/PeakCalling/")
	print "Step5 : Peak Calling for each files achieved..."
	print ""
	print "Step6 : IDR analysis..."
	if idr == 'OFF':
		print "Skipped"
	else:
		createOdir(outputdir+"/IDR")
		consistency(rep1, rep2, ctrlfile, outputdir)
		consistency(prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		consistency(prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		consistency(prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz", ctrlfile, outputdir)
		nt = countConsistentPeaks(rep1, rep2, outputdir, idrthresh)
		np = countConsistentPeaks(prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz", outputdir, idrthresh)
		n1 = countConsistentPeaks(prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", outputdir , idrthresh)
		n2 = countConsistentPeaks(prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", outputdir , idrthresh)
		exportResults(nt, np, n1, n2, outputdir)
		print "Step6 : IDR analysis achieved..."
	print ""
	print "Step7 : Plotting IDR results..."
	if plot == 'OFF':
		print "Skipped"
	else:
		createOdir(outputdir+"/IDR/plots")
		plotResults(outputdir, rep1, rep2, prefixr1+"_PR1.tagAlign.gz", prefixr1+"_PR2.tagAlign.gz", prefixr2+"_PR1.tagAlign.gz", prefixr2+"_PR2.tagAlign.gz", prefixpool+"_PR1.tagAlign.gz", prefixpool+"_PR2.tagAlign.gz")
		print "Step7 : Plotting IDR results achieved..."
	print ""
	print "Step8 : Creating final sets of peaks..."
	if finalsets == 'OFF':
		print "Skipped"
	else:
		createOdir(outputdir+"/finalsets")
		createFinalSets(poolfile , ctrlfile, nt, np, outputdir, prefix)
		print "Step8 : Creating final sets of peaks achieved..."
	goodbyeCp()
	return