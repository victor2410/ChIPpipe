#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# AnnoPeaks.py
# ======================
# Author: Gaborit Victor
# Date: Jun 30, 2016
# ======================

"""
	Package to annotate ChIP-seq Peaks with ChromHMM results
"""

# Packages required for this programm

import os
import sys
from print_message import usageAp, welcomeAp, parametersAp, running, summaryAp, goodbyeCp
from set_default import initParamAp, createOdir
from get_opt import readOptAp
from check import checkRequiredAp
from transform import toCoordFile
from export import exportProm, exportEnh
from Annotate import annotatePeaks
from produce_plot import plotAnno
from count import countLines

def mainAp(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageAp()
		sys.exit(1)
	outputdir, selectodir, peakfile, annofile, peakcaller, prefix, graph = initParamAp() # intialize to default all parameters
	outputdir, selectodir, peakfile, annofile, peakcaller, prefix, graph = readOptAp(argv[1:], outputdir, selectodir, peakfile, annofile, peakcaller, prefix, graph)
	checkRequiredAp(peakfile, annofile, peakcaller)
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeAp() # print welcome message
	if prefix ==  '': # If no prefix is given in the command line, give a default prefix
		prefix = 'AnnoPeaks'
	parametersAp(outputdir, peakfile, annofile, peakcaller, prefix) # print a summary of all parameters used
	running() # print running message
	print ""
	print "Step1 : Transforming peak file to coordinate file..."
	peakfile = toCoordFile(peakfile, outputdir, prefix)
	print "Step1 : Transforming peak file to coordinate file achieved..."
	print ""
	print "Step2 : Extract promoter regions from annotation file..."
	exportProm(annofile, outputdir)
	print "Step2 : Extract promoter regions from annotation file achieved..."
	print ""
	print "Step3 : Extract enhancer regions from annotation file..."
	exportEnh(annofile, outputdir)
	print "Step3 : Extract enhancer regions from annotation file achieved..."
	print ""
	print "Step4 : Annotate peaks that falls into promoter regions..."
	promfile = annotatePeaks(peakfile, outputdir, outputdir+"/promoter_region.bed", prefix)
	print "Step4 : Annotate peaks that falls into promoter regions achieved..."
	print ""
	print "Step5 : Annotate peaks that falls into enhancer regions..."
	enhfile = annotatePeaks(peakfile, outputdir, outputdir+"/enhancer_region.bed", prefix)
	print "Step5 : Annotate peaks that falls into enhancer regions achieved..."
	print ""
	nbpeak = countLines(peakfile)
	nbprom = countLines(promfile)
	nbenh = countLines(enhfile)
	summaryAp(nbpeak, nbprom, nbenh)
	print ""
	print "Step 6 : Plotting annotation results..."
	if graph == 'OFF':
		print "Skipped"
	else:
		plotAnno(nbpeak, nbprom, nbenh, outputdir)
		print "Step 6 : Plotting annotation results achieved..."
	goodbyeCp()
	return