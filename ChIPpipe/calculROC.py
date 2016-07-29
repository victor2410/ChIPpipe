#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# calculROC.py
# ======================
# Author: Gaborit Victor
# Date: Jul 25, 2016
# ======================

"""
	Functions to calculate AUC and create ROC curve
"""

# packages required for this programm

from shlex import split
import subprocess
from set_default import getPrefix
import os

def scoreAUC(scorefile, outputdir):
	aucfile = getPrefix(scorefile)
	outfile = outputdir+"/"+aucfile+"_AUC.txt"
	command = "Rscript $RCHIPpipe_PATH/Calculate_AUC.r -i="+scorefile+" "+outfile
	subprocess.call(command, shell=True)
	return