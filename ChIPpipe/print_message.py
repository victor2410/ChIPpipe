#!/usr/bin/python3.4
# -*-coding:utf-8 -*


# print_message.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
  	Functions to print differents message to stdout :

  	- Usage
  	- Title of the programm
  	- Parameters settled
  	- Running
  	- End of the programm
"""

def usageCa():
	print "ChIPalign, ChIP-seq tool for alignment and filtration of reads"
	print "Usage : ChIPpipe ChIPalign [-f <path/file.fastq(.gz)> | -1 <path/fileR1.fastq(.gz)> -2 <path/file2.fastq(.gz)>] -g <path/GenomeDirectory/prefix> [options]"
	print "\t-h, --help 	: print this usage message."
	print "\nREQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of single end fastq file to analyze(must be .fastq or .fastq.gz)"
	print "\t or"	
	print "\t-1 FILE1 -2 FILE2	: full path and name of fastq file for reads 1 (-1) and reads 2 (-2) for paired end datas to analyze(must be .fastq or .fastq.gz)"
	print "\t-g GENOMEPREFIX	: full path and prefix of file containing all sequnces from reference chromosomes of genome used(without extension .fa or .fasta) (exemple : hg19_AllChr)"
	print "\nOPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files(default create a new repositorie in the current directory)"
	print "\t--index	: indexing genome files, must be select if the genome have not been indewed before(defaut : OFF)"
	print "\t-q INT : reads filtering according to the minimum mapping quality specified\n"
	print "\t-F : filter out unmapped reads"
	print "\t-L FILE : remove reads mapped in coordinate files given(blacklist)"
	print "\t--rmdup : remove PCR duplicates and non unique mappable reads"
	print "\t--sort : sort final bam file\n"
	print "\t--bamIndex : indexing final bam file (requiring --sort)"
	print "\t--name NAME : prefix to give to output files"

def usageCp():
	print "CallPeaks, PeakCalling tool related on spp and ENCODE IDR analysis pipeline"
	print "Usage : ChIPpipe CallPeaks -1 <path/fileRep1.tagAlign(.gz)> -2 <path/fileRep2.tagAlign(.gz)> --c1 <path/fileControl.tagAlign.gz> [options]"
	print "\t-h, --help 	: usage."
	print "REQUIRED ARGUMENTS"
	print "\t-1 FILE_REP1	: full path and name of replicate 1 file (bam file)"
	print "\t-2 FILE_REP2	: full path and name of replicate 2 file (bam file)"
	print "\t--c1 FILE_CONTROL	:  full path and name of control file (bam file)"
	print "OPTIONNAL ARGUMENTS"
	print "\t--c2 FILE_CONTROL	:  full path and name of second control file (if there is one) (bam file)"
	print "\t-o <path/directory>	: full path to directory in wich write all output files (default create a CallPeaks_out directory in the current directory)"
	print "\t--idr FLOAT	: Perform IDR analysis on output peakCalling files with a specified threshold (0.01 or 0.02 for transcription factor) (default : OFF)"
	print "\t--sets	: Create final peak sets (conservative and optimum) corresponding to IDR threshold (require --idr option) (default :OFF)"
	print "\t--no-plots	: Do not plot IDR results (default : ON)"
	print "\t--name NAME : prefix to give to output files (default is CallPeaks)"
	print "\t--version : version of this programm"

def usageCpnr():
	print "CallPeaks_norep, PeakCalling for sample without biological replicates related on MACS2"
	print "Usage : ChIPpipe CallPeaks_norep -f <path/file.bam>-c <path/control.bam> [options]"
	print "\t-h, --help 	: usage"
	print "REQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of alignment file to analyze (bam format)"
	print "\t-c FILE	: full path and name of Input alignment file to use (bam format)"
	print "OPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)"
	print "\t--thresh STR	: pvalue threshold for peak calling (ex : 1e-7 ; default = 1e-3)"
	print "\t--nomodel	: using estimated fragment length by phantomPeakQualtools for peakCalling than macs2 prediction model"
	print "\t--name NAME : prefix to give to output files (default is CallPeaks_macs)"

def usage():
	print "usage ChIPpipe [-h] [--version]"
	print "\t{ChIPalign, CallPeaks, CallPeaks_norep}"
	print ""
	print "ChIPpipe, pipeline for alignment and peak calling of ChIP-Seq datas"
	print ""
	print "POSITIONAL COMMANDS:"
	print "\tChIPalign\tAlignment and filtration of ChIP-Seq fastq"
	print "\tCallPeaks\tPeakCalling based on IDR analysis protocol proposed by ENCODE (requiring biological replicates)"
	print "\tCallPeaks_norep\tPeakCalling when no biological replicates are available"
	print ""
	print "OPTIONAL ARGUMENTS"
	print "\t-h, --help 	: usage."
	print "\t--version : version of ChIPpipe"


def welcomeCa():
	print ""
	print "\t#############"
	print "\t# ChIPalign #"
	print "\t#############"
	print ""
	print "\tChIPalign, ChIP-seq tool for alignment and filtration of reads"

def welcomeCp():
	print ""
	print "\t#############"
	print "\t# CallPeaks #"
	print "\t#############"
	print ""
	print "\tCallPeaks, PeakCalling tool related on spp and ENCODE IDR analysis pipeline"

def welcomeCpnr():
	print ""
	print "\t###################"
	print "\t# CallPeaks_norep #"
	print "\t###################"
	print ""
	print "\tCallPeaks_norep, PeakCalling for sample without biological replicates related on MACS2"

def parametersSe(fastqfile, genome, outputdir, filterqual, minqual, unmapped, filtercoord, coordinateFile, indexGenome, rmvdup, sorting, indexBam, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "fastq file to align :"+fastqfile
	print "fasta file for reference genome :"+genome+".fa"
	print "output directory :"+outputdir
	print "prefix name to give to output files :"+prefix
	print "genome indexing :"+indexGenome
	if filterqual == 'OFF':
		print "filtering with minimum mapping quality :"+filterqual
	else:
		print "filtering with minimum mapping quality :"+filterqual
		print "mapping quality threshold :"+minqual
	print "filtering unmapped reads :"+unmapped
	if filtercoord == 'OFF':
		print "filtering reads inside coordinates files :"+filtercoord
	else:
		print "filtering reads inside coordinates files :"+filtercoord
		print "coordinates files to filter out :"+coordinateFile
	print "remove PCR duplicates and non uniquely mappable reads :"+rmvdup
	print "sorting final bam file :"+sorting
	print "indexing final bam file :"+indexBam

def parametersPe(fastqfile1, fastqfile2, genome, outputdir, filterqual, minqual, unmapped, filtercoord, coordinateFile, indexGenome, rmvdup, sorting, indexBam, prefix):
	print ""
	print "################################"
	print "# PARAMETERS USED FOR THIS RUN #"
	print "################################"
	print ""
	print "fastq file R1 to align :"+fastqfile1
	print "fastq file R2 to align :"+fastqfile2
	print "fasta file for reference genome :"+genome+".fa"
	print "output directory :"+outputdir
	print "prefix name to give to output files :"+prefix
	print "genome indexing :"+indexGenome
	if filterqual == 'OFF':
		print "filtering with minimum mapping quality :"+filterqual
	else:
		print "filtering with minimum mapping quality :"+filterqual
		print "mapping quality threshold :"+minqual
	print "filtering unmapped reads :"+unmapped
	if filtercoord == 'OFF':
		print "filtering reads inside coordinates files :"+filtercoord
	else:
		print "filtering reads inside coordinates files :"+filtercoord
		print "coordinates files to filter out :"+coordinateFile
	print "remove PCR duplicates and non uniquely mappable reads :"+rmvdup
	print "sorting final bam file :"+sorting
	print "indexing final bam file :"+indexBam

def parametersCp(outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "bam file Replicate 1 :"+rep1
	print "bam file Replicate 2 :"+rep2
	print "bam file Control :"+ctrl1
	if ctrlsup == 'true':
		print "bam file Control supp. :"+ctrl2
	print "output directory :"+outputdir
	print "prefix name to give to output files :"+prefix
	if idr == 'OFF':
		print "Run IDR analysis :"+idr
	else:
		print "Run IDR analysis :"+idr
		print "IDR threshold :"+idrthresh
	print "Creating final set of peaks:"+finalsets
	print "Plotting IDR results :"+plot

def parametersCpnr(outputdir, selectodir, bamfile, ctrlfile, thresh, model, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "bam file :"+bamfile
	print "bam file Control :"+ctrlfile
	print "output directory :"+outputdir
	print "prefix name to give to output files :"+prefix
	if model == 'OFF':
		print "estimate fragment length related on phantomPeakQualtools"
	else:
		print "let macs2 build model itself for estimating peakCalling parameters"
	print "p-value threshold fo peakCalling:"+thresh

def running():
	print ""
	print "\t###################"
	print "\t# RUNNIG ANALYSIS #"
	print "\t###################"
	print ""

def goodbyeCa(bamname):
	print ""
	print "Final alignment file can be found at :"+bamname
	print "All of specified steps have been performed, exiting..."
	print ""
	print "\t#####################"
	print "\t# ANALYSIS ACHIEVED #"
	print "\t#####################"

def goodbyeCp():
	print ""
	print "All of specified steps have been performed, exiting..."
	print ""
	print "\t#####################"
	print "\t# ANALYSIS ACHIEVED #"
	print "\t#####################"


