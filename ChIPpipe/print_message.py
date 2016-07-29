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

def usageTq(): 
	print "TrimQual, quality check and trimming tools for ChIP-seq fastq files"
	print "Usage : ChIPpipe trimQual [-f path/file.fastq(.gz)> | -1 <path/fileR1.fastq(.gz)> -2 <path/fileR2.fastq(.gz)>] --lib INT [options]"
	print "\t-h, --help 	: print this usage message"
	print "\nREQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of single end fastq file to analze (could be .fastq or .fastq.gz)"
	print "\t or"	
	print "\t-1 FILE_R1 -2 FILE_R2	: full path and name of fastq file R1 (-1) and R2 (-2) for paired end data (could be .fastq or .fastq.gz)"
	print "\--lib INT	: select the adaptator library following used sequencer (0: Illumina Genome Analyzer IIx ; 1: Hi Seq 2000)"
	print "\nOPTIONNAL ARGUMENTS"
	print "\t-o DIRECTORY	: output directory in which put all output files (default create trimQual_out in current directory)"	
	print "\t--adapt <PE|SE>	: Sequencing library used for adaptators (default depend on -f (SE) or -1 (PE) options)"	

def usageCa():
	print "ChIPalign, ChIP-seq tool for alignment and filtration of reads"
	print "Usage : ChIPpipe ChIPalign [-f <path/file.fastq(.gz)> | -1 <path/fileR1.fastq(.gz)> -2 <path/file2.fastq(.gz)>] -g <path/GenomeDirectory/prefix> [options]"
	print "\t-h, --help 	: print this usage message"
	print "\nREQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of single end fastq file to analyze(must be .fastq or .fastq.gz)"
	print "\t or"	
	print "\t-1 FILE1 -2 FILE2	: full path and name of fastq file for reads 1 (-1) and reads 2 (-2) for paired end datas to analyze(must be .fastq or .fastq.gz)"
	print "\t-g GENOMEPREFIX	: full path and prefix of file containing all sequnces from reference chromosomes of genome used(without extension .fa or .fasta) (exemple : hg19_AllChr)"
	print "\nOPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files(default create a new repositorie in the current directory)"
	print "\t--index	: indexing genome files, must be select if the genome have not been indewed before(defaut : OFF)"
	print "\t-q INT : reads filtering according to the minimum mapping quality specified"
	print "\t-F : filter out unmapped reads"
	print "\t-L FILE : remove reads mapped in coordinate files given(blacklist)"
	print "\t--rmdup : remove PCR duplicates and non unique mappable reads"
	print "\t--sort : sort final bam file"
	print "\t--bamIndex : indexing final bam file (requiring --sort)"
	print "\t--name NAME : prefix to give to output files"

def usageCp():
	print "CallPeaks, PeakCalling tool related on spp and ENCODE IDR analysis pipeline"
	print "Usage : ChIPpipe CallPeaks -1 <path/fileRep1.bam> -2 <path/fileRep2.bam> --c1 <path/fileControl.bam> [options]"
	print "\t-h, --help 	: print this usage message"
	print "REQUIRED ARGUMENTS"
	print "\t-1 FILE_REP1	: full path and name of replicate 1 file (bam file)"
	print "\t-2 FILE_REP2	: full path and name of replicate 2 file (bam file)"
	print "\t--c1 FILE_CONTROL	:  full path and name of control file (bam file)"
	print "OPTIONNAL ARGUMENTS"
	print "\t--c2 FILE_CONTROL	:  full path and name of second control file (if there is one) (bam file)"
	print "\t-o <path/directory>	: full path to directory in wich write all output files (default create a CallPeaks_out directory in the current directory)"
	print "\t--idr FLOAT	: Perform IDR analysis on output peakCalling files with a specified threshold (0.01 or 0.02 for transcription factor) (default: OFF)"
	print "\t--sets	: Create final peak sets (conservative and optimum) corresponding to IDR threshold (require --idr option) (default: OFF)"
	print "\t--no-plots	: Do not plot IDR results (default : ON)"
	print "\t--name NAME : prefix to give to output files (default is CallPeaks)"

def usageCpnr():
	print "CallPeaks_norep, PeakCalling for sample without biological replicates related on MACS2"
	print "Usage : ChIPpipe CallPeaks_norep -f <path/file.bam>-c <path/control.bam> [options]"
	print "\t-h, --help 	: print this usage message"
	print "REQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of alignment file to analyze (bam format)"
	print "\t-c FILE	: full path and name of Input alignment file to use (bam format)"
	print "OPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)"
	print "\t-p 	: call peaks based on pvalue threshold (default: ON)"
	print "\t-q 	: call peaks based on qvalue threshold (default: OFF)"
	print "\t--thresh STR	: pvalue threshold for peak calling (ex : 1e-7 ; default = 1e-3)"
	print "\t--spp-qual	: Cross-correlation analysis performed by spp before calling peaks (default: OFF)"
	print "\t--name NAME : prefix to give to output files (default is CallPeaks_macs)"

def usageAp():
	print "AnnoPeaks, Peaks annotation based on ChromHMM results to annotate promoter and enhancer Transcription factor binding site"
	print "Usage : ChIPpipe AnnoPeaks -f <path/peakfile> -a <path/ChrommHMMannotationFile.bed> --peakCaller <spp|macs2> [options]"
	print "\t-h, --help 	: print this usage message"
	print "REQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of peak file "
	print "\t-a FILE	: full path and name of ChromHMM annotation file (bed file)"
	print "OPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)"
	print "\t--plot	: for plotting annotation results (default is off)"
	print "\t--name NAME : prefix to give to output files (default is AnnoPeaks)"

def usageMd():
	print "MotifDiscover, Motif discovery tool related on MEME suite"
	print "Usage : ChIPpipe MotifDiscover -f <path/regionFile.bed> -g <path/genomeFile[.fa|.fasta]>[options]"
	print "\t-h, --help 	: print this usage message"
	print "REQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of region bed file "
	print "\t-g FILE	: full path and name of genome fasta file (could be .fa or .fasta extension)"
	print "OPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)"
	print "\t--name NAME : prefix to give to output files (default is MotifDiscover)"
	print "\t--db STRING : database to use to perform central enrichment analysis and motif scanning (default is OFF) must be JASPAR, HUMAN or UNIPROBE"

def usageSm():
	print "ScanMotif, Motif enrichment analysis tool related on HOMER"
	print "Usage : ChIPpipe MotifDiscover -f <path/regionFile.bed> -g <path/genomeFile[.fa|.fasta]> -m <path/motifFile.motif>[options]"
	print "\t-h, --help 	: print this usage message"
	print "REQUIRED ARGUMENTS"
	print "\t-f FILE	: full path and name of region bed file "
	print "\t-g FILE	: full path and name of genome fasta file (could be .fa or .fasta extension)"
	print "\t-m FILE 	: full path and name of motif file (with .motif extension)"
	print "OPTIONNAL ARGUMENTS"
	print "\t-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)"
	print "\t--name NAME : prefix to give to output files (default is MotifDiscover)"
	print "\t--excl STRING : genomic region to exclude from background file (EXON: refseq coding exon; BLACKLIST: consensus hg19 blacklist region; BOTH) (default include those regions)"

def usage():
	print "usage ChIPpipe [-h] [--version]"
	print "\t{trimQual, ChIPalign, CallPeaks, CallPeaks_norep, AnnoPeaks, MotifDiscover, ScanMotif}"
	print ""
	print "ChIPpipe, pipeline for alignment, peak calling, annotation and motif analysis of ChIP-Seq datas"
	print ""
	print "POSITIONAL COMMANDS:"
	print "\ttrimQual\tQuality check and trimming of ChIP-seq fastq"
	print "\tChIPalign\tAlignment and filtration of ChIP-Seq fastq"
	print "\tCallPeaks\tPeakCalling based on IDR analysis protocol proposed by ENCODE (requiring biological replicates)"
	print "\tCallPeaks_norep\tPeakCalling when no biological replicates are available"
	print "\tAnnoPeaks\tAnnotate ChIP-seq peaks with ChromHMM annotation file"
	print "\tMotifDiscover\tMotif discovery related on MEME suite"
	print "\tScanMotif\tMotif enrichment analysis related on HOMER"
	print ""
	print "OPTIONAL ARGUMENTS"
	print "\t-h, --help 	: print this usage message"
	print "\t--version : version of ChIPpipe"

def welcomeTq():
	print ""
	print "\t############"
	print "\t# trimQual #"
	print "\t############"
	print ""
	print "\tTrimQual, quality check and trimming tools for ChIP-seq fastq files"

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

def welcomeAp():
	print ""
	print "\t#############"
	print "\t# AnnoPeaks #"
	print "\t#############"
	print ""
	print "\tAnnoPeaks, Peaks annotation based on ChromHMM results to annotate promoter and enhancer Transcription factor binding site"

def welcomeMd():
	print ""
	print "\t#################"
	print "\t# MotifDiscover #"
	print "\t#################"
	print ""
	print "\tMotifDiscover, Motif discovery tool related on MEME suite"

def welcomeSm():
	print ""
	print "\t#############"
	print "\t# ScanMotif #"
	print "\t#############"
	print ""
	print "\tScanMotif, Motif enrichment analysis tool related on HOMER"


def parametersTq(outputdir, fastqfile, fastqfile1, fastqfile2, adaptaters, lib, seq1, seq2):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	if seq1 == 'SE':
		print "\tfastq file: "+fastqfile
		print "\tdatas are Single End"
	else:
		print "\tfastq file R1: "+fastqfile1
		print "\tfastq file R2: "+fastqfile2
		print "\tdatas are paired end"
	print "\toutput directory: "+outputdir
	if int(lib) == 0:
		print "\tsequencer used to get reads: Illumina Genome Analyzer IIx"
	else:
		print "\tsequencer used to get reads: Hi Seq 2000"
	if seq2 != '':
		if seq2 == 'SE':
			print "\tsearching for single end adaptator"
		else:
			print "\tsearching for paired end adaptator"
	print "\ttrimmomatic adaptator library: "+adaptaters

def parametersSe(fastqfile, genome, outputdir, filterqual, minqual, unmapped, filtercoord, coordinateFile, indexGenome, rmvdup, sorting, indexBam, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tfastq file to align: "+fastqfile
	print "\tfasta file for reference genome: "+genome+".fa"
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix
	print "\tgenome indexing: "+indexGenome
	if filterqual == 'OFF':
		print "\tfiltering with minimum mapping quality: "+filterqual
	else:
		print "\tfiltering with minimum mapping quality: "+filterqual
		print "\tmapping quality threshold: "+minqual
	print "\tfiltering unmapped reads: "+unmapped
	if filtercoord == 'OFF':
		print "\tfiltering reads inside coordinates files: "+filtercoord
	else:
		print "\tfiltering reads inside coordinates files: "+filtercoord
		print "\tcoordinates files to filter out: "+coordinateFile
	print "\tremove PCR duplicates and non uniquely mappable reads: "+rmvdup
	print "\tsorting final bam file: "+sorting
	print "\tindexing final bam file: "+indexBam

def parametersPe(fastqfile1, fastqfile2, genome, outputdir, filterqual, minqual, unmapped, filtercoord, coordinateFile, indexGenome, rmvdup, sorting, indexBam, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tfastq file R1 to align: "+fastqfile1
	print "\tfastq file R2 to align: "+fastqfile2
	print "\tfasta file for reference genome: "+genome+".fa"
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix
	print "\tgenome indexing: "+indexGenome
	if filterqual == 'OFF':
		print "\tfiltering with minimum mapping quality: "+filterqual
	else:
		print "\tfiltering with minimum mapping quality: "+filterqual
		print "\tmapping quality threshold: "+minqual
	print "\tfiltering unmapped reads: "+unmapped
	if filtercoord == 'OFF':
		print "\tfiltering reads inside coordinates files: "+filtercoord
	else:
		print "\tfiltering reads inside coordinates files: "+filtercoord
		print "\tcoordinates files to filter out: "+coordinateFile
	print "\tremove PCR duplicates and non uniquely mappable reads: "+rmvdup
	print "\tsorting final bam file: "+sorting
	print "\tindexing final bam file: "+indexBam

def parametersCp(outputdir, selectodir, rep1, rep2, ctrl1, ctrl2, ctrlsup, idr, idrthresh, finalsets, plot, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tbam file Replicate 1: "+rep1
	print "\tbam file Replicate 2: "+rep2
	print "\tbam file Control: "+ctrl1
	if ctrlsup == 'true':
		print "\tbam file Control supp: "+ctrl2
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix
	if idr == 'OFF':
		print "\tRun IDR analysis: "+idr
	else:
		print "\tRun IDR analysis: "+idr
		print "\tIDR threshold: "+idrthresh
	print "\tCreating final set of peaks: "+finalsets
	print "\tPlotting IDR results: "+plot

def parametersCpnr(outputdir, bamfile, ctrlfile, thresh, pvalue, qvalue, qc, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tbam file: "+bamfile
	print "\tbam file Control: "+ctrlfile
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix
	print "\tCross-correlation analysis before calling peaks (performed by spp): "+qc
	if pvalue == 'ON':
		print "\tpeakcalling based on p-value"
		print "\tp-value threshold fo peakCalling: "+thresh
	else:
		print "\tpeakcalling based on q-value"
		print "\tq-value threshold fo peakCalling: "+thresh

def parametersAp(outputdir, peakfile, annofile, peakcaller, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tpeak file: "+peakfile
	print "\tchromHMM annotation file: "+annofile
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix

def parametersMd(outputdir, regionfile, genomefile, database, scan, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tregion file: "+regionfile
	print "\tgenome file: "+genomefile
	if scan == 'ON':
		print "\tcentral enrichment and motif scanning performed by CentriMo and Tomtom will be performed"
		print "\tdatabase to use: "+database
	else:
		print "\tOnly perform de novo motif discovery"
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix

def parametersSm(outputdir, regionfile, genomefile, motiffile, exclude, prefix):
	print ""
	print "\t################################"
	print "\t# PARAMETERS USED FOR THIS RUN #"
	print "\t################################"
	print ""
	print "\tregion file: "+regionfile
	print "\tgenome file: "+genomefile
	print "\tmotif file: "+motiffile
	print "\tgenomic region to exclude when genrating background: "+exclude
	print "\toutput directory: "+outputdir
	print "\tprefix name to give to output files: "+prefix

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

def summaryAp(nbpeak, nbprom, nbenh):
	print "Number of total peaks :"+str(nbpeak)
	print "Number of peaks that fall into promoter regions :"+str(nbprom)
	print "Number of peaks that fall into enhancer regions :"+str(nbenh)