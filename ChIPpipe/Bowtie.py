#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# Bowtie.py
# ======================
# Author: Gaborit Victor
# Date: Jun 22, 2016
# ======================

"""
    Functions calling bowtie2 tools to do :
 
   	- Genome Indexing
   	- Read alignment from fastq files
"""

# Packages required for this programm

import subprocess
import os

def genomeIndex(settings, genome): # Function for indexing reference genome
	print ""
	print "Step1 : Genome Indexing..."
	if settings == 'OFF': # This step is optionnal, if it is not set, it will be skipped
		print "skipped"
	else:
		print "Calling bowtie2-build..."
		fasta = genome+".fa"
		subprocess.check_call(['bowtie2-build', fasta, genome]) # Indexing genome with command line : "bowtie2-build fasta genome" where fasta is the fasta files of the genome and genome is the prefix to give to output files
		print "Step1 : Genome indexing achieved..."
	return

def readsAlignment(seq, fastqfile, fastqfile1, fastqfile2, outputdir, genome, prefix): # Function for reads alignment versus reference genome
	print ""
	print "Step2 : Reads Alignment..." 
	samout = outputdir+"/"+prefix+".sam" # create file name for temporary sam file
	bamout = outputdir+"/"+prefix+".bam" # create file name for final bam file
	print "Output name :"+bamout
	if seq == 'SE': # If one fastq file is given with the '-f' option, indicating that the reads are single end 
		print "Alignement for single end reads..."
		subprocess.check_call(['bowtie2', '-x', genome, '-U', fastqfile, '-p', '4', '-S', samout]) # Alignment with command line : "bowtie2 -x genome -U fastqfile -p 4 -S samout"
	else: # Two fastq files are given so the reads are paired end
		print "Alignment for paired end reads..." # the command are the same than for SE alignment excepting that two fastq files are required
		subprocess.check_call(['bowtie2', '-x', genome, '-1', fastqfile1, '-2', fastqfile2, '-p', '4', '-S', samout]) # "bowtie2 -x genome -1 fasqtfile1 -2 fastqfile2 -p 4 -S samout"
	subprocess.check_call([ 'samtools', 'view', samout, '-bS', '-o', bamout]) # Transformation from sam file to bam file with command line : "samtools view samout -bS -o bamout"
	os.remove(samout) # removing temporary sam file
	print "Step2 : Reads Alignment achieved..."
	return bamout # return the name of the final bam file