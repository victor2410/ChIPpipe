#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# genereFile.py
# ======================
# Author: Gaborit Victor
# Date: Jul 25, 2016
# ======================

"""
	Functions to create new files
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix
import os

def createBackground(regionfile, exclude, outputdir, prefix):
	print ""
	chrlength = '$RCHIPpipe_PATH/hg19_table.txt'
	outfile = outputdir+"/BG_"+prefix+".bed"
	if exclude != 'NONE':
		if exclude == 'BOTH':
			exclfile1 = '$RCHIPpipe_PATH/coding_exons.bed'
			exclfile2 = '$RCHIPpipe_PATH/consensusBlacklist.bed'
			command = "bedtools shuffle -i "+regionfile+" -g "+chrlength+" -excl "+exclfile1+" -excl "+exclfile2+" > "+outfile
			print "\tGenomic region file 1 to exclude: "+exclfile1
			print "\tGenomic region file 2 to exclude: "+exclfile2
		elif exclude == 'EXON':
			exclfile1 = '$RCHIPpipe_PATH/coding_exons.bed'
			command = "bedtools shuffle -i "+regionfile+" -g "+chrlength+" -excl "+exclfile1+" > "+outfile
			print "\tGenomic region file to exclude: "+exclfile1
		else:
			exclfile2 = '$RCHIPpipe_PATH/consensusBlacklist.bed'
			command = "bedtools shuffle -i "+regionfile+" -g "+chrlength+" -excl "+exclfile2+" > "+outfile
			print "\tGenomic region file to exclude: "+exclfile2
	else:
		command = "bedtools shuffle -i "+regionfile+" -g "+chrlength+" > "+outfile
		print "\tGenerate background on whole genome"
	print "\tGenerating background region file..."
	subprocess.call(command, shell=True)
	print "\tAchieved"
	print ""
	return outfile

def createScoreFile(scanfile, scanbgfile, motiffile, outputdir, prefix):
	motifname = getPrefix(motiffile)
	outfile = outputdir+"/"+prefix+"_Score_"+motifname+".txt"
	command1 = "cat "+scanfile+" | grep \"^chr\" | cut -f 6 | awk \'{print $0\"\t\"1}\' > "+outfile
	command2 = "cat "+scanbgfile+" | grep \"^chr\" | cut -f 6 | awk \'{print $0\"\t\"0}\' >> "+outfile
	subprocess.call(command1, shell=True)
	subprocess.call(command2, shell=True)
	return outfile
	