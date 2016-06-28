#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# IDRanalysis.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

# Packages required for this programm
from subprocess import Popen, PIPE
from shlex import split
import subprocess
from set_default import getPrefix

def consistency(file1, file2, control, outputdir):
	print ""
	print "IDR analysis for :"+file1+" vs "+file2+"..."
	tmp1 = getPrefix(file1)
	tmp2 = getPrefix(file2)
	tmpctrl = getPrefix(control)
	file_in1 = outputdir+"/PeakCalling/"+tmp1+".tagAlign_VS_"+tmpctrl+".tagAlign.regionPeak.gz"
	file_in2 = outputdir+"/PeakCalling/"+tmp2+".tagAlign_VS_"+tmpctrl+".tagAlign.regionPeak.gz"
	outname = outputdir+"/IDR/"+tmp1+"_VS_"+tmp2 
	command = "Rscript $RCHIPpipe_PATH/batch-consistency-analysis.r "+file_in1+" "+file_in2+" -1 "+outname+" 0 F signal.value $RCHIPpipe_PATH/functions-all-clayton-12-13.r $RCHIPpipe_PATH/genome_table.txt"
	subprocess.call(command, shell=True)
	print "Done"
	return

def countConsistentPeaks(file1, file2, outputdir, thresh):
	tmp1 = getPrefix(file1)
	tmp2 = getPrefix(file2)
	file_name = outputdir+"/IDR/"+tmp1+"_VS_"+tmp2+"-overlapped-peaks.txt"
	f = open(file_name,'r')
	lines  = f.readlines()
	f.close()
	numb = 0
	for line in lines:
		value = line.split(" ", 13)
		if len(value) == 11:
			if float(value[10]) <= float(thresh):
				numb += 1
	return numb