#!/usr/bin/python3.4
# -*-coding:utf-8 -*


# sorting.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================


"""
    Functions calling for sorting and indexing final bam file :

    - Sorting bam file 
    - Indexing bam file
"""

# Packages required for this programm

import subprocess
import os

def sortAndIndexFile(settingssort, settingsindex, outputdir, bamname, prefix):
	print ""
	print "Step7 : Sorting alignment file per position..."
	if settingssort == 'OFF': # Optional so if is not specified, skip this step
		print "skipped"
		bamout = outputdir+"/"+prefix+".bam"
		os.rename(bamname, bamout) # Rename final bam file
		print "" # If no sort, can't do the indexing of bam file
		print "Step8 : Indexing final alignment file..."
		print "skipped"
	else:
		bamout = outputdir+"/"+prefix+"_sorted.bam"
		subprocess.check_call(['samtools', 'sort', bamname, '-o', bamout]) # command line : "samtools sort bamname -o bamout"
		print "Final number of reads in alignement file: "
		subprocess.check_call([ 'samtools', 'view', bamout, '-c'])  # count the number of reads in the final file
		os.remove(bamname)
		print "Step7 : Sorting alignment file per position achieved..."
		indexFile(settingsindex, outputdir, bamout) # calling function for indexing final bam file
	return bamout

def indexFile(settings, outputdir, bamname): # Create an index for the final alignment file with samtools
	print ""
	print "Step8 : Indexing final alignment file..."
	if settings == 'OFF': # Optional so if is not specified, skip this step
		print "skipped"
	else:
		subprocess.check_call(['samtools', 'index', bamname]) # command line : "samtools index bamname"
		print "Step8 : Indexing final alignment file achieved..."