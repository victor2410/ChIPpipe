#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# Callspp.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
	Package to perform total peak calling in CallPeaks script 
	or to perform only cross correlation analysis on CallPeaks_norep script
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix


def peakCall(file_in, control, outputdir): # Perform all peak calling with spp
	print ""
	print "Peak calling for :"+file_in+"..."
	outname = outputdir+getPrefix(file_in)
	command = "Rscript $RCHIPpipe_PATH/run_spp.R -c="+file_in+" -i="+control+" -npeak=300000 -odir="+outputdir+" -savr -savp -rf -out="+outname+"_stats.tab > "+outname+"_peakCalling.log"
	subprocess.call(command, shell=True)
	print "Done"
	return

def estimateParam(chipfile, outputdir, prefix): # only perform cross correlation analysis to estimate parameters
	print ""
	command1 = "Rscript $RCHIPpipe_PATH/run_spp_nodups.R -c="+chipfile+" -savp -out="+outputdir+"/"+prefix+".tab"
	subprocess.call(command1, shell=True)
	myfile = open(outputdir+prefix+".tab", "r")
	text = myfile.read()
	myfile.close
	line = text.split("\t", 4)
	temp = line[2]
	fragmentsize = temp.split(",", 3)
	print "Estimated fragment length :"+fragmentsize[0]
	halffrag=(int(fragmentsize[0])+1)/2
	print "half fragment size :"+str(halffrag)
	return int(fragmentsize[0]), halffrag