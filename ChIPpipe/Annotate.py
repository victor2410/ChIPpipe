#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# Annotate.py
# ======================
# Author: Gaborit Victor
# Date: Jun 30, 2016
# ======================

"""
	Package to annotate ChIP-seq Peaks with coordinate file
"""

# Packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix
from check import checkGz
import os

def annotatePeaks(filein, outputdir, annofile, prefix):
	print ""
	print "searching for peaks in "+filein+" that fall into "+annofile+" region file..."
	tmp = getPrefix(annofile)
	command = "bedtools intersect -a "+filein+" -b "+annofile+" -wa -f 0.51 | sort -k1,1 -k2,2n | uniq > "+outputdir+"/"+prefix+"_"+tmp+".bed"
	subprocess.call(command, shell=True)
	print "Done"
	print "Annotated file can be found at :"+outputdir+"/"+prefix+"_"+tmp+".bed"
	return outputdir+"/"+prefix+"_"+tmp+".bed"