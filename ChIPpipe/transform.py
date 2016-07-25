#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# transform.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
	Package to convert file in different format and rename file
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix
from check import checkGz
import os

def toTagAlign(file_in, outputdir): # convert given bam file to tagAlign file
	filename = getPrefix(file_in)
	tagAlignname = outputdir+filename+".tagAlign.gz"
	print "Transformation for file :"+file_in+"..."
	COMMAND = "samtools view -b "+file_in+"|bamToBed -i stdin|awk 'BEGIN{FS=\"\t\";OFS=\"\t\"}{$4=\"N\"; print $0}'|gzip -c > "+tagAlignname
	subprocess.call(COMMAND, shell=True)
	print "Transformation achieved..."
	return

def toCoordFile(peakfile, outputdir, prefix):
	if checkGz(peakfile) == True:
		print "Compressed file given, will have to unzipp it..."
		command = "zcat "+peakfile+" > "+outputdir+"/tmp_peakfile.bed"
		subprocess.call(command, shell=True)
	else:
		command = "cat "+peakfile+" > "+outputdir+"/tmp_peakfile.bed"
		subprocess.call(command, shell=True)
	tmpfile = outputdir+"/tmp_peakfile.bed"
	outputfile = outputdir+"/"+prefix+"_coord.bed"
	f = open(tmpfile,'r') # open resulting file
	lines  = f.readlines()
	f.close()
	o = open(outputfile, 'w')
	for line in lines:
		value = line.split("\t", 15)
		o.write(str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\n")
	o.close()
	os.remove(tmpfile)
	return outputfile


def newName(file_in, outputdir): # get new tagAlign file name
	fileprefix = getPrefix(file_in)
	newname = outputdir+fileprefix+".tagAlign.gz"
	return newname
