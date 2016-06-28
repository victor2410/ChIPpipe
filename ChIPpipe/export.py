#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# export.py
# ======================
# Author: Gaborit Victor
# Date: Jun 28, 2016
# ======================

# Packages required for this programm
import os

def exportResults(nt, np, n1, n2, outputdir):
	fileout = open(outputdir+"/IDR/idrResults.tab", "w")
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
	fileout.close()
	print "IDR results could be found at :"+outputdir+"/IDR/idrResults.tab"
	return