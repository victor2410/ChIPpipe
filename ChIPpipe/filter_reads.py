#!/usr/bin/python3.4
# -*-coding:utf-8 -*


# filter_reads.py
# ======================
# Author: Gaborit Victor
# Date: Jun 21, 2016
# ======================


"""
    Packages calling for filter out reads from bam file :
 
   	- Unmapped reads
   	- Reads with low mapping quality
   	- PCR duplicates and non uniquely mappable reads
   	- Reads in blacklist regions
"""

# packages required for this programm

import subprocess
import os

def unmappedFilter(settings, outputdir, bamname, prefix): # Filter out unmapped reads in alignment file with samtools
	print ""
	print "Step3 : Filtering out unmapped reads..."
	bamout = bamname
	if settings == 'OFF': # Optional so if is not specified, skip this step
		print "skipped"
	else:
		bamout = outputdir+"/"+prefix+"mapped.bam" 
		subprocess.check_call([ 'samtools', 'view', '-F', '4', bamname, '-b', '-o', bamout]) # command line : "samtools view -F 4 bamname -b -o bamout" 
		print "number of reads after removing unmapped reads: "
		subprocess.check_call([ 'samtools', 'view', bamout, '-c']) # count the number of reads in the filtered file
		os.remove(bamname) # remove previous bamfile
		print "Step3 : Filtering out unmapped reads achieved..."
	return bamout # return name of current bam file

def minQFilter(settings, thresh, outputdir, bamname, prefix): # Filter out reads with mapping quality lower than a specified threshold in alignment file with samtools

	print ""
	print "Step4 : Filtering out reads with low mapping quality..."
	bamout = bamname
	if settings == 'OFF': # Optional so if is not specified, skip this step
		print "skipped"
	else:
		print "mapping quality threshold: "+str(thresh)
		bamout = outputdir+"/"+prefix+"highmQ.bam"
		subprocess.check_call([ 'samtools', 'view', '-q', thresh, bamname, '-b', '-o', bamout])  # command line : "samtools view -q bamname -b -o bamout" 
		print "number of reads after removing reads with low mapping quality: "
		subprocess.check_call([ 'samtools', 'view', bamout, '-c']) # count the number of reads in the filtered file
		os.remove(bamname) # remove previous bamfile
		print "Step4 : Filtering out reads with low quality achieved..."
	return bamout

def removeDup(settings, outputdir, bamname, prefix): # Remove PCR duplicates and non uniquely mapable reads in alignment file with picard MarkDuplicates
	print ""
	print "Step5 : Filtering out PCR duplicates and non uniquely mapable reads..."
	bamout = bamname
	if settings == 'OFF': # Optional so if is not specified, skip this step
		print "skipped"
	else:
		tempbam = outputdir+"/"+prefix+"temp.bam"
		bamout = outputdir+"/"+prefix+"rmdup.bam"
		picardinput = 'I='+tempbam
		picardoutput = 'O='+bamout
		subprocess.check_call(['samtools', 'sort', bamname, '-o', tempbam]) # For using picard MarkDuplicates a sorting bam file is required
		os.remove(bamname) # remove previous bamfile
		subprocess.check_call(['picard-tools', 'MarkDuplicates', picardinput, picardoutput, 'M=tmp.txt', 'REMOVE_DUPLICATES=true']) # command line "picard-tools MarkDuplicates I=tempbam O=bamout M=tmp.txt REMOVE_DUPLICATES=true"
		os.remove('tmp.txt') # remove temporary files
		os.remove(tempbam)
		print "number of reads after removing PCR duplicates and non uniquely mappable reads: "
		subprocess.check_call([ 'samtools', 'view', bamout, '-c']) # count the number of reads in the filtered file
		print "Step5 : Filtering out PCR duplicates and non uniquely mapable reads achieved..."
	return bamout

def coordFilter(settings, coordinatefile, outputdir, bamname, prefix): # Filter out reads that overlapp with blacklist regions with samtools
	print ""
	print "Step6 : Filtering out reads mapped inside blacklist regions..."
	bamout = bamname
	if settings == 'OFF': # Optional so if is not specified, skip this step
		print "skipped"
	else:
		print "blacklist coordinates file: "+coordinatefile
		bamout = outputdir+"/"+prefix+"keeped.bam"
		tempbam = outputdir+"/"+prefix+"blacklist.bam"
		subprocess.check_call([ 'samtools', 'view', bamname, '-L', coordinatefile, '-U', bamout , '-b', '-o', tempbam]) # command line : "samtools view bamname -L coordinatefile -U bamout -b -o tempbam" 
		print "number of reads after removing reads inside blacklist regions: "
		subprocess.check_call([ 'samtools', 'view', bamout, '-c']) # count the number of reads in the filtered file
		os.remove(tempbam) # Remove temporary file and previous bam file
		os.remove(bamname)
		print "Step6 : Filtering out reads mapped inside blacklist regions achieved..."
	return bamout