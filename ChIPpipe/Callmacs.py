#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# CallPeaks_norep.py
# ======================
# Author: Gaborit Victor
# Date: Jun 27, 2016
# ======================

"""
	Package to call macs2 following the specified parameters
"""

# packages required for this programm

from shlex import split
import subprocess

def peakCallMacs(chipfile, ctrlfile, outputdir, prefix, pvalue, qvalue, thresh): # peak calling 
	if pvalue == 'ON':
		command = "macs2 callpeak -t "+chipfile+" -c "+ctrlfile+" -f BED -n "+outputdir+"/"+prefix+" -g hs -p "+thresh+" --to-large -B --outdir "+outputdir+"/PeakCalling/"
		subprocess.call(command, shell=True)
	else:
		command = "macs2 callpeak -t "+chipfile+" -c "+ctrlfile+" -f BED -n "+outputdir+"/"+prefix+" -g hs -q "+thresh+" --to-large -B --outdir "+outputdir+"/PeakCalling/"
		subprocess.call(command, shell=True)