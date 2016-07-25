#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# ChIPpipe.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
   Main wrapper for pipeline to analyze ChIP-Seq datas, 4 subfunctions :
    - trimQual
   	- ChIPalign
   	- CallPeaks
   	- CallPeaks_norep
   	- AnnoPeaks
"""

# Packages required for this programm

import sys
from ChIPalign import mainCa
from CallPeaks import mainCp
from CallPeaks_norep import mainCpnr
from trimQual import mainTq
from print_message import usage
from get_opt import readOpt
from AnnoPeaks import mainAp


__all__ = ['main']
def main():
	if len(sys.argv) == 1: # if any arguments are given print usage message and then exit the programm
		usage()
		sys.exit(1)
	readOpt(sys.argv[1:]) # read the options present in command line argument
	if sys.argv[1] == 'ChIPalign': # Call to ChIPalign tool
		mainCa(sys.argv[1:])
	elif sys.argv[1] == 'CallPeaks': # Call to CallPeaks tool
		mainCp(sys.argv[1:])
		sys.exit(0)
	elif sys.argv[1] == 'CallPeaks_norep': # Call to CallPeaks_norep tool
		mainCpnr(sys.argv[1:])
	elif sys.argv[1] == 'trimQual': # Call to trimQual tool
		mainTq(sys.argv[1:])
	elif sys.argv[1] == 'AnnoPeaks':
		mainAp(sys.argv[1:])
	else: # Wrong parameter specified, print usage message and then exit
		print "Wrong parameter specified, please check your options"
		usage()
		sys.exit(0)


if __name__ == "__main__": # If this script is called we execute the main function
    main()
    sys.exit(0)
