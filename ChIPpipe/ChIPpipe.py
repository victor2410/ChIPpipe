#!/usr/bin/python3.4
# -*-coding:utf-8 -*

# ChIPpipe.py
# ======================
# Author: Gaborit Victor
# Date: Jun 23, 2016
# ======================

"""
   Main wrapper for pipeline to analyze ChIP-Seq datas, 3 subfunctions :
   	- ChIPalign
   	- CallPeaks
   	- CallPeaks_norep
"""

# Packages required for this programm

import sys
from ChIPalign import mainCa
from CallPeaks import mainCp
from CallPeaks_norep import mainCpnr
from print_message import *
from get_opt import *


__all__ = ['main']
def main():
	if len(sys.argv) == 1: # if any arguments are given print usage message and then exit the programm
		usage()
		sys.exit(1)
	readOpt(sys.argv[1:])
	if sys.argv[1] == 'ChIPalign':
		mainCa(sys.argv[1:])
	elif sys.argv[1] == 'CallPeaks':
		print "still in implementation for now..."
		mainCp(sys.argv[1:])
		sys.exit(0)
	elif sys.argv[1] == 'CallPeaks_norep':
		mainCpnr(sys.argv[1:])


if __name__ == "__main__": # If this script is called we execute the main function
    main()
    sys.exit(0)
