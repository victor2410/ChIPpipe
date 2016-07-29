#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# ScanMotif.py
# ======================
# Author: Gaborit Victor
# Date: Jul 25, 2016
# ======================

"""
	Package to perform motif enrichment analysis related on HOMER
"""

# Packages required for this programm

import os
import sys
from print_message import usageSm, welcomeSm, parametersSm, running
from set_default import initParamSm, createOdir
from get_opt import readOptSm
from check import checkRequiredSm
from transform import toFastaFile
from motif import motifDeNovo, motifFull, scanSeqMotif
from genereFile import createBackground, createScoreFile
from sorting import sortScoreFile
from calculROC import scoreAUC


def mainSm(argv):
	if len(argv) == 1: # if any arguments are given print usage message and then exit the programm
		usageSm()
		sys.exit(1)
	outputdir, selectodir, regionfile, genomefile, motiffile, exclude, prefix = initParamSm() # intialize to default all parameters
	outputdir, selectodir, regionfile, genomefile, motiffile, exclude, prefix = readOptSm(argv[1:], outputdir, selectodir, regionfile, genomefile, motiffile, exclude, prefix)
	checkRequiredSm(regionfile, genomefile, motiffile)
	if selectodir == 'false': # If no output directory specified, create one folder in current directory
		createOdir(outputdir)
	welcomeSm() # print welcome message
	parametersSm(outputdir, regionfile, genomefile, motiffile, exclude, prefix) # print a summary of all parameters used
	running() # print running message
	print ""
	print "Step1: Generate random background region..."
	backgroundfile = createBackground(regionfile, exclude, outputdir, prefix)
	print "Step1: Generate random background region achieved..."
	print ""
	print "Step2: Transforming region bed file to fasta file..."
	fastafile = toFastaFile(regionfile, genomefile, outputdir, prefix)
	print "Step2: Transforming region bed file to fasta file achieved..."
	print ""
	print "Step3: Transforming background bed file to fasta file..."
	bgfastafile = toFastaFile(backgroundfile, genomefile, outputdir, "BG_"+prefix)
	print "Step3: Transforming background bed file to fasta file achieved..."
	print ""
	print "Step4: Scanning foreground sequence with motif file..."
	scanfile = scanSeqMotif(fastafile, motiffile, outputdir, prefix)
	print "Step4: Scanning foreground sequence with motif file achieved..."
	print ""
	print "Step5: Scanning background sequence with motif file..."
	scanbgfile = scanSeqMotif(bgfastafile, motiffile, outputdir, "BG_"+prefix)
	print "Step5: Scanning background sequence with motif file achieved..."
	print ""
	print "Step6: Creating score file for motif enrichment..."
	scorefile = createScoreFile(scanfile, scanbgfile, motiffile, outputdir, prefix)
	print "Step6: Creating score file for motif enrichment achieved..."
	print ""
	print "Step7: Sorting score file..."
	scorefile = sortScoreFile(scorefile, outputdir)
	print "Step7: Sorting score file achieved..."
	print ""
	print "Step8: Calculate AUC for motif enrichment..."
	scoreAUC(scorefile, outputdir)
	print "Step8: Calculate AUC for motif enrichment achieved..."
	print ""
	return