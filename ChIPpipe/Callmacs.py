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


def peakCallMacs1(chipfile, ctrlfile, outputdir, prefix, thresh, halffrag, fragmentsize): # peak calling without gives to parameters (let macs2 estimate it itself)
	command = "macs2 callpeak -t "+chipfile+" -c "+ctrlfile+" -f BED -n "+outputdir+prefix+" -g hs -p "+thresh+" --to-large --nomodel --shift "+str(halffrag)+" --extsize "+str(fragmentsize)+" -B"
	subprocess.call(command, shell=True)

def peakCallMacs2(chipfile, ctrlfile, outputdir, prefix, thresh):
	command = "macs2 callpeak -t "+chipfile+" -c "+ctrlfile+" -f BED -n "+outputdir+prefix+" -g hs -p "+thresh+" --to-large -B"
	subprocess.call(command, shell=True)