#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# check.py
# ======================
# Author: Gaborit Victor
# Date: Jun 22, 2016
# ======================

"""
    Functions calling for checking differents parameters :
 
   	- Check if a file exist
   	- Check if a directory exists
   	- Check if a given file is in a fastq format
   	- Check if a genome fasta file exists
   	- Check if required options are specified
"""

# packages required for this programm

import os
import sys

def checkFile(file_in): # Check the existence of a file
	if not os.path.isfile(file_in): # If the file not exists, print an error message then exit the programm
		print "Error, the specified file '"+file_in+"' does not exists"
		sys.exit(1)
	return

def checkPath(path_in): # Check if a full path exists
	if not os.path.exists(path_in): # If a part or all the path does not exists, return false
		return False
	return True

def checkFastq(fastqfile): # Check if a given file is in fastq format
	checkFile(fastqfile) # Check if the file exist
	fastqext = os.path.splitext(fastqfile) 
	if fastqext[1] == '.gz': # if the file is compressed the last extension is '.gz', so we have to check the extension before 
		fastqext = os.path.splitext(fastqext[0])
		if fastqext[1] == '.fastq': # If the extension before is '.fastq', the file exists and is in right format, we quit this function to continue
			return
		else: # If the extension before is different of '.fastq', print an error message and exit the programm
			print "Error the specified file '"+fastqfile+"' is not in fastq format"
			sys.exit(1)
	elif fastqext[1] == '.fastq': # if the last extension is '.fastq', the file is not compressed but is still in the right format, we quit this function to conitnue
		return
	else: # The extension is different whatever it is, print an error message and then exit the programm
		print "Error the specified file '"+fastqfile+"' is not in fastq format"
		sys.exit(1)
	return

def checkBam(bamfile): # Check if a given file is in fastq format
	checkFile(bamfile) # Check if the file exist
	fileext = os.path.splitext(bamfile) 
	if fileext[1] == '.bam': # if the extension is '.bam', the file is in the right format, quit this function and continue 
		return
	else: # The extension is different whatever it is, print an error message and then exit the programm
		print "Error the specified file '"+bamfile+"' is not in fastq format"
		sys.exit(1)
	return

def checkBed(bedfile): # Check if a given file is in fastq format
	checkFile(bedfile) # Check if the file exist
	fileext = os.path.splitext(bedfile) 
	if fileext[1] == '.bed': # if the extension is '.bam', the file is in the right format, quit this function and continue 
		return
	else: # The extension is different whatever it is, print an error message and then exit the programm
		print "Error the specified file '"+bedfile+"' is not in fastq format"
		sys.exit(1)
	return

def checkGz(filein): # Check if a given file is in fastq format
	fileext = os.path.splitext(filein) 
	if fileext[1] == '.gz': # if the extension is '.bam', the file is in the right format, quit this function and continue 
		return True
	else: # The extension is different whatever it is, print an error message and then exit the programm
		return False

def checkGenome(genomefile): # Check the existence of fasta file genome
	genome = genomefile + ".fa" 
	if os.path.isfile(genome): # If the file exist with '.fa' extension, quit the function and continue
		return
	genome = genomefile + ".fasta"
	if os.path.isfile(genome): # If not exists with '.fa' extension , try with '.fasta' extension, if exists, quit the function and then continue
		return
	else: # If not exists with '.fasta' extension, mean that the genome files is not in the right format, print an error message and then exit the programm
		print "Error, the specified file '"+genomefile+"' cannot be find"
		sys.exit(1)
	return

def checkLib(lib): # check if the integer specified is 0 or 1
	if int(lib) != 0 and int(lib) != 1: # if integer not expected, print an error message and then exit the programm
		print "Error, library must be 0 for 1 or sequencer used, please check with -h option"
		sys.exit(1)
	return

def checkRequiredTq(fastqfile, fastqfile1, fastqfile2, lib): # Check if all required option are specified
	if fastqfile1 == '' and fastqfile2 == '': # means that no options '-1' and '-2' have been specified
		if fastqfile == '': # means that no options '-f' have been specified, print an error message and exit the programm
 			print "Error the options -f or -1 and -2 have not been used, these option are required to run this programm"
			sys.exit(1)
	elif fastqfile != '': # means that '-f', '-1' an '-2' options have been used together, print an error message and then exit
		print "Error the options -f or -1 and -2 have been used together, use -f option alone or -1 and -2 option together"
		sys.exit(1)
	if lib == 2: # means that '--lib options have not been used'
		print "Error, option --lib is required to perform this analyze"
		sys.exit(1)
	return

def checkRequiredCa(seq, fastqfile2, genome): # Check if all required option are specified
	if seq == '': # means that no options '-f' or '-1/-2' have been specified, print an error message and exit the programm
 		print "Error no options -f or -1 and -2 have been used, these option are required to run this programm"
		sys.exit(1)
	elif seq == 'PE': # means that seq is 'PE' or 'SE' (two choices possible), if is 'SE' so '-f' option is used, if is 'PE' at least '-1' option is used
		if fastqfile2 == '': # if '-1' option is used, check if '-2' option is also used, if not, print an error message and exit the programm
			print "Error it seems that the option -1 have been used without using -2 option. If you only have one fastq, please re-run with the option -f or if you have one fastq R1 and one fastq R2, please re-run with -1 fastqR1 and -2 fastqR2"
			sys.exit(1)
	if genome == '': # if no genome prefix have been specified, means that required '-g' options have not been used, print an error message and then exit the programm
		print "Error, a reference genome file is required to perform this analysis, please re-run with the option -g"
		sys.exit(1)
	return

def checkRequiredCp(rep1, rep2, ctrl1): # Check if all required option are specified
	if rep1 == '': # means that no options '-1' have been specified, print an error message and exit the programm
 		print "Error the options -1 have not been used, this option are required to run this programm"
		sys.exit(1)
	if rep2 == '': # means that no options '-2' have been specified, print an error message and exit the programm
		print "Error the options -2 have not been used, this option are required to run this programm"
		sys.exit(1)
	if ctrl1 == '': # means that no control file is given , print an error message and exit the programm
		print "Error, at least one control file (input) is expected to perform this analysis, please re-run with the option --c1"
		sys.exit(1)
	return

def checkRequiredCpnr(file_in, ctrl): # Check if all required option are specified
	if file_in == '' or ctrl == '': # means that no options '-1' have been specified, print an error message and exit the programm
 		print "Error the options -f or -c or both have not been used, these option are required to run this programm"
		sys.exit(1)
	return

def checkRequiredAp(peakfile, annofile, peakcaller): # Check if all required option are specified
	if peakfile == '': # means that no options '-f' have been specified, print an error message and exit the programm
 		print "Error the options -f have not been used, this option are required to run this programm"
		sys.exit(1)
	if annofile == '': # means that no options '-a' have been specified, print an error message and exit the programm
		print "Error the options -a have not been used, this option are required to run this programm"
		sys.exit(1)
	return