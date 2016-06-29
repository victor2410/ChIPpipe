#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# Callfastqc.py
# ======================
# Author: Gaborit Victor
# Date: Jun 29, 2016
# ======================

"""
   Main package for calling fastqc tool
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix


def fastQc(fastqfile, outputdir):
	print "running fastqc tool for : "+fastqfile+"..."
	prefix = getPrefix(fastqfile)
	command = "fastqc -o "+outputdir+"/fastqc_report/ "+fastqfile
	subprocess.call(command, shell=True)
	f = open(outputdir+"/fastqc_report/"+prefix+"_fastqc/summary.txt",'r') # open resulting file
	lines  = f.readlines()
	f.close()
	find = False
	nbwarn = 0
	for line in lines: # for each line, if the 1st column is FAIL, then print which test is failed
		value = line.split("\t", 4)
		if value[0] == 'FAIL':
			find = True
			print value[1]+" have failed quality check"
		elif value[0] == 'WARN':
			nbwarn += 1
	if find == False:
		print "Any test failed quality check"
	print str(nbwarn)+" tests present warnings"
	print "Done"
	return