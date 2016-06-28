#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# plot.py
# ======================
# Author: Gaborit Victor
# Date: Jun 28, 2016
# ======================

# Packages required for this programm
from subprocess import Popen, PIPE
from shlex import split
import subprocess
import os
from set_default import getPrefix

def plotResults(outputdir, rep1, rep2, rep1pr1, rep1pr2, rep2pr1, rep2pr2, poolpr1, poolpr2):
	print "Plotting IDR results for "+rep1+" and "+rep2+"..."
	tmp1 = getPrefix(rep1)
	tmp2 = getPrefix(rep2)
	fileout = outputdir+"/IDR/plots/"+tmp1+"_VS_"+tmp2
	filename = outputdir+"/IDR/"+tmp1+"_VS_"+tmp2
	command1 = "Rscript $RCHIPpipe_PATH/batch-consistency-plot.r 1 "+fileout+" "+filename+" $RCHIPpipe_PATH/functions-all-clayton-12-13.r"
	command2 = "Rscript $RCHIPpipe_PATH/IDR_results_plots.r -r="+filename+"-overlapped-peaks.txt -o="+fileout
	subprocess.call(command1, shell=True)
	subprocess.call(command2, shell=True)
	print "Done"
	print "Plotting IDR results for pseudo-replicates...."
	tmp1 = getPrefix(rep1pr1)
	tmp2 = getPrefix(rep1pr2)
	tmp3 = getPrefix(rep2pr1)
	tmp4 = getPrefix(rep2pr2)
	fileout = outputdir+"/IDR/plots/pseudo-replicates"
	fileout1 = outputdir+"/IDR/plots/"+tmp1+"_VS_"+tmp2
	fileout2 = outputdir+"/IDR/plots/"+tmp3+"_VS_"+tmp4
	filename1 = outputdir+"/IDR/"+tmp1+"_VS_"+tmp2
	filename2 = outputdir+"/IDR/"+tmp3+"_VS_"+tmp4
	command1 = "Rscript $RCHIPpipe_PATH/batch-consistency-plot.r 2 "+fileout+" "+filename1+" "+filename2+" $RCHIPpipe_PATH/functions-all-clayton-12-13.r"
	command2 = "Rscript $RCHIPpipe_PATH/IDR_results_plots.r -r="+filename1+"-overlapped-peaks.txt -o="+fileout1
	command3 = "Rscript $RCHIPpipe_PATH/IDR_results_plots.r -r="+filename1+"-overlapped-peaks.txt -o="+fileout2
	subprocess.call(command1, shell=True)
	subprocess.call(command2, shell=True)
	subprocess.call(command3, shell=True)
	print "Done"
	print "Plotting IDR results for pool pseudo-replicates..."
	tmp1 = getPrefix(poolpr1)
	tmp2 = getPrefix(poolpr2)
	fileout = outputdir+"/IDR/plots/"+tmp1+"_VS_"+tmp2
	filename = outputdir+"/IDR/"+tmp1+"_VS_"+tmp2
	command1 = "Rscript $RCHIPpipe_PATH/batch-consistency-plot.r 1 "+fileout+" "+filename+" $RCHIPpipe_PATH/functions-all-clayton-12-13.r"
	command2 = "Rscript $RCHIPpipe_PATH/IDR_results_plots.r -r="+filename+"-overlapped-peaks.txt -o="+fileout
	subprocess.call(command1, shell=True)
	subprocess.call(command2, shell=True)
	print "Done"
	return