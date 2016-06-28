#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# CallPeaks_norep.py
# ======================
# Author: Gaborit Victor
# Date: Jun 27, 2016
# ======================

# Packages required for this programm

from subprocess import Popen, PIPE
from shlex import split
import subprocess
from set_default import getPrefix


def peakCallMacs1(chipfile, ctrlfile, outputdir, prefix, thresh, halffrag, fragmentsize):
	command = "macs2 callpeak -t "+chipfile+" -c "+ctrlfile+" -f BED -n "+outputdir+prefix+" -g hs -p "+thresh+" --to-large --nomodel --shift "+str(halffrag)+" --extsize "+str(fragmentsize)+" -B"
	subprocess.call(command, shell=True)

def peakCallMacs2(chipfile, ctrlfile, outputdir, prefix, thresh):
	command = "macs2 callpeak -t "+chipfile+" -c "+ctrlfile+" -f BED -n "+outputdir+prefix+" -g hs -p "+thresh+" --to-large -B"
	subprocess.call(command, shell=True)