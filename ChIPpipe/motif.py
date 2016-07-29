#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# motif.py
# ======================
# Author: Gaborit Victor
# Date: Jul 26, 2016
# ======================

"""
	Functions related on motif discovery and finding
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix, createOdir
import os

def motifFull(fastafile, outputdir, database, prefix):
	if database == 'JASPAR':
		dataname = '$RCHIPpipe_PATH/motifs_database/JASPAR_CORE_2016.meme'
	elif database == 'HUMAN':
		dataname = '$RCHIPpipe_PATH/motifs_database/HOCOMOCOv10_HUMAN_mono_meme_format.meme'
	else:
		dataname = '$RCHIPpipe_PATH/motifs_database/TFBSshape_UniPROBE.meme'
	print ""
	print "\tDatabase selected: "+dataname 
	print "\tPerforming motif discovery and scanning..."
	command = "meme-chip "+fastafile+" -oc "+outputdir+"/"+prefix+"/ -db "+dataname+" -meme-minw 6 -meme-maxw 20 -meme-nmotifs 5 -fimo-skip -spamo-skip"
	subprocess.call(command, shell=True)
	print "Analysis achieved"
	print ""
	return

def motifDeNovo(fastafile, outputdir, prefix):
	print ""
	print "\tPerforming motif discovery..."
	command = "meme-chip "+fastafile+" -oc "+outputdir+"/"+prefix+"/ -meme-minw 6 -meme-maxw 20 -meme-nmotifs 5 -fimo-skip -spamo-skip"
	subprocess.call(command, shell=True)
	print "Analysis achieved"
	print ""
	return

def scanSeqMotif(sequencefile, motiffile, outputdir, prefix):
	motifname = getPrefix(motiffile)
	outfile = outputdir+"/"+prefix+"_"+motifname+".txt"
	createOdir(outputdir+"/"+prefix+"_"+motifname)
	command = "findMotifs.pl "+sequencefile+" fasta "+outputdir+"/"+prefix+"_"+motifname+"/ -find "+motiffile+" > "+outfile
	subprocess.call(command, shell=True)
	return outfile

