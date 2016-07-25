#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# export.py
# ======================
# Author: Gaborit Victor
# Date: Jun 28, 2016
# ======================

"""
	Package used to export results to file 
"""

# packages required for this programm

import os
import re

def exportResults(nt, np, n1, n2, outputdir):
	fileout = open(outputdir+"/IDR/idrResults.tab", "w") # open output file
	fileout.write("Nt\tNp\tN1\tN2\tNp/Nt\tN1/N2\tNumber of peaks (conservative)\tNumber of peaks (optimum)\n")
	if n1 == 0 or n2 == 0:
		selfcons = 0
	elif n1 > n2:
		selfcons = n1/n2
	else:
		selfcons = n2/n1
	if nt > np:
		opt = nt
		cons = nt/np
	else:
		opt = np
		cons = np/nt
	fileout.write(str(nt)+"\t"+str(np)+"\t"+str(n1)+"\t"+str(n2)+"\t"+str(cons)+"\t"+str(selfcons)+"\t"+str(nt)+"\t"+str(opt))
	fileout.close() # close output file
	print "IDR results could be found at :"+outputdir+"/IDR/idrResults.tab"
	return

def exportProm(annofile, outputdir):
	print ""
	filein = open(annofile, 'r')
	lines = filein.readlines()
	filein.close()
	fileout = open(outputdir+"/promoter_region.bed", 'w')
	nbline = 1
	for line in lines:
		if int(nbline) == 1:
			nbline += 1
			continue
		else:
			value = line.split("\t", 15)
			if re.match(r"^.*[pP]romoter.*$", value[3]):
				fileout.write(value[0]+"\t"+value[1]+"\t"+value[2]+"\n")
			else:
				continue
	fileout.close()
	print "promoter region file can be found at :"+outputdir+"/promoter_region.bed"
	print ""
	return


def exportEnh(annofile, outputdir):
	print ""
	filein = open(annofile, 'r')
	lines = filein.readlines()
	filein.close()
	fileout = open(outputdir+"/enhancer_region.bed", 'w')
	nbline = 1
	for line in lines:
		if int(nbline) == 1:
			nbline += 1
			continue
		else:
			value = line.split("\t", 15)
			if re.match(r"^.*[eE]nhancer.*$", value[3]):
				fileout.write(value[0]+"\t"+value[1]+"\t"+value[2]+"\n")
			else:
				continue
	fileout.close()
	print "enhancer region file can be found at :"+outputdir+"/enhancer_region.bed"
	print ""
	return