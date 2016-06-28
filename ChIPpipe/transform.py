#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# transform.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

# Packages required for this programm
from subprocess import Popen, PIPE
from shlex import split
import subprocess
from set_default import getPrefix

def toTagAlign(file_in, outputdir):
	filename= getPrefix(file_in)
	tagAlignname = outputdir+filename+".tagAlign.gz"
	print "Transformation for file :"+file_in+"..."
	COMMAND = "samtools view -b "+file_in+"|bamToBed -i stdin|awk 'BEGIN{FS=\"\t\";OFS=\"\t\"}{$4=\"N\"; print $0}'|gzip -c > "+tagAlignname
	subprocess.call(COMMAND, shell=True)
	print "Transformation achieved..."
	return

def newName(file_in, outputdir):
	fileprefix = getPrefix(file_in)
	newname = outputdir+fileprefix+".tagAlign.gz"
	return newname
