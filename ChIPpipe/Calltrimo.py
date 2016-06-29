#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# Calltrimo.py
# ======================
# Author: Gaborit Victor
# Date: Jun 29, 2016
# ======================

"""
   Main package for calling trimmomatic
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix
import os

def trimmoSe(fastqfile, outputdir, adapter):
	print ""
	tmp1 = getPrefix(fastqfile)
	command1 = "zcat "+fastqfile+" | head -n 2 | tail -n 1 > "+outputdir+"/temp.txt"
	subprocess.call(command1, shell=True)
	f = open(outputdir+"/temp.txt",'r') # open resulting file
	lines  = f.readlines()
	f.close()
	for line in lines:
		readlength = len(line)-1
	os.remove(outputdir+"/temp.txt")
	print "read length for this file: "+str(readlength)
	fileout = outputdir+"/fastq_trim/"+tmp1+"_trim.fastq.gz"
	command2 = "java -jar $RCHIPpipe_PATH/Trimmomatic-0.35/trimmomatic-0.35.jar SE -phred33 "+fastqfile+" "+fileout+" ILLUMINACLIP:$RCHIPpipe_PATH/Trimmomatic-0.35/adapters/"+adapter+":2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:"+str(readlength)
	subprocess.call(command2, shell=True)
	return fileout

def trimmoPe():
	print ""