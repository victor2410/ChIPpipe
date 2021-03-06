#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# final.py
# ======================
# Author: Gaborit Victor
# Date: Jun 28, 2016
# ======================

"""
	Package for creating final peaks sets
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix

def createFinalSets(poolfile, control, nt, np, outputdir, prefix):
	print "Creating conservative peak set..."
	tmp = getPrefix(poolfile)
	tmpctrl = getPrefix(control)
	filein = outputdir+"/PeakCalling/"+tmp+".tagAlign_VS_"+tmpctrl+".tagAlign.regionPeak.gz"
	fileout = outputdir+"/finalsets/"+prefix+"_spp_conservative.regionPeak.gz"
	command = "zcat "+filein+"|sort -k7nr,7nr|head -n "+str(nt)+"|gzip -c > "+fileout # get only the nt first peaks
	subprocess.call(command, shell=True)
	print "Done"
	print "Creating optimum peak set..."
	fileout = outputdir+"/finalsets/"+prefix+"_spp_optimum.regionPeak.gz"
	maxnum = max(nt, np)
	command = "zcat "+filein+"|sort -k7nr,7nr|head -n "+str(maxnum)+"|gzip -c > "+fileout # get only the max(nt, np) first peaks
	subprocess.call(command, shell=True)
	print "Done"
	return

def createFinalSets2(chipfile, control, np, outputdir, prefix):
	print "Creating peak set..."
	tmp = getPrefix(chipfile)
	tmpctrl = getPrefix(control)
	filein = outputdir+"/PeakCalling/"+tmp+".tagAlign_VS_"+tmpctrl+".tagAlign.regionPeak.gz"
	fileout = outputdir+"/finalsets/"+prefix+"_spp.regionPeak.gz"
	command = "zcat "+filein+"|sort -k7nr,7nr|head -n "+str(np)+"|gzip -c > "+fileout # get only the np first peaks
	subprocess.call(command, shell=True)
	print "Done"
	return