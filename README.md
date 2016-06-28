# ChIPpipe, python package for ChIP-seq files analyze

##########
# Author #
##########

For questions, comments that you should be interesting for improve this pipeline, please send email to victor.gaborit2@gmail.com
see also:

-> samtools documentation : http://samtools.sourceforge.net/

-> bowtie2 documentation : http://bowtie-bio.sourceforge.net/bowtie2/index.shtml

-> picard-tools documentation : https://broadinstitute.github.io/picard/

-> python documentation : https://www.python.org/

-> spp documentation : http://compbio.med.harvard.edu/Supplements/ChIP-seq/

-> macs2 documentation : https://github.com/taoliu/MACS

-> ENCODE IDR analysis : https://sites.google.com/site/anshulkundaje/projects/idr


################
# Presentation #
################

This pipeline is created to perform full analysis of ChIP-seq datas. This pipeline is only automatization of existing tools or pipelines created to perform ChIP-seq datas analysis in particular case there is no biological replicates. There are three differents programm in this pipeline :

	-> ChIPalign : Alignment and filtration of ChIP-seq fastq files
	-> CallPeaks : Peak Calling based on ENCODE protocol with IDR analysis (requiring replicates)
	-> CallPeaks_norep : Peak Calling related on macs2 and used when no replicates are available

This pipeline is implemented in python.

##################
# Required tools #
##################

To run this pipeline, these tools are required :
 
	-bowtie2 (v2.1.0)
		from shell terminal:
		sudo apt-get install bowtie2
	-samtools (v1.3.1)
		from shell terminal:
		sudo apt-get install samtools
	-picard tools (v1.95)
		from shell terminal:
		sudo apt-get install picard-tools
	-spp (v1.10.1) 
		from shell terminal:
		cd path/to/ChIPpipe/Scripts
		R CMD INSTALL spp_1.10.1.tar.gz
	-python (<=v2.7)
	-R (v3.0.2)
		All .r and .R scripts required are present in the folder Rscripts

All of this three tools must be accessible in your environment variable.

################
# Installation #
################

After installed all the required tools, got to ChIPalign directory and install it with python.
	from shell terminal:
		cd /Path/to/ChIPpipe
		sudo python setup.py install
This will add to your environment variable the command ChIPalign.
You also need to indicate path to Rscripts in your .bashrc
	from shell terminal:
		cd $HOME
		gedit .bashrc
	Add the following line:
		export RCHIPpipe_PATH = "/fullpath/to/ChIPpipe/Scripts"
	then from shell terminal:
		source ~.bashrc

#########
# Usage #
#########

from shell terminal launch :

		ChIPpipe
		or
		ChIPpipe -h 
		or 
		ChIPpipe --help

this will print to screen the usage message :

		usage ChIPpipe [-h] [--version]
		{ChIPalign, CallPeaks, CallPeaks_norep}

		ChIPpipe, pipeline for alignment and peak calling of ChIP-Seq datas

		POSITIONAL COMMANDS:
			ChIPalign	Alignment and filtration of ChIP-Seq fastq
			CallPeaks	PeakCalling based on IDR analysis protocol proposed by ENCODE (requiring biological replicates)
			CallPeaks_norep	PeakCalling when no biological replicates are available

		OPTIONAL ARGUMENTS
			-h, --help 	: usage.
			--version : version of ChIPpipe


Check software version 

		ChIPpipe --version
			ChIPpipe.0.0.1


#########
# Usage #
#########

ChIPalign:
	
	Call :

		ChIPpipe ChIPalign [-f FILE.fastq | -1 FILE_R1.fastq -2 FILE_R2.fastq] -g GENOME_PREFIX [options]
--name NAME : prefix to give to output files
	Required arguments:

		-f FASTQ_FILE : full path and name of single end fastq file
		or
		-1 FASTQ_FILE_R1 and -2 FASTQ_FILE_R2 : full path and name of paired end R1 and R2 files
		-g GENOME_PREFIX: full path and prefix of genome reference fasta file (without '.fa' or '.fasta' extension)

	Optionnal arguments :

		-o DIRECTORY : to specify the place you want your output files in (default : create ChIPalign_out in current directory)
		--name PREFIX : prefix name to give to output files (default is fastqfile prefix)
		--index : index the reference genome (required for alignment but just need to be done once) (default : OFF)
		-q INT : filter reads with mapping quality lower than specific threshold (INT) (default : OFF)
		-F : filter unmapped reads (default : OFF)
		-L FILE : filter reads that mapp inside specific regions like blacklist regions given in specified FILE (default : OFF)
		--rmdup : filter PCR duplicates and non uniquely mapable reads (default : OFF)
		--sort : sort final bam file per reads position (default : OFF)
		--bamIndex : index final bam file (required --sort option) (default : OFF)
	
##########
# Output #
##########


ChIPalign:

	This pipeline will produce in a directory (depend on -o option) a unique bam file named PREFIX.bam and an indexed bam file named PREFIX.bam.bai (if --bamIndex was specified).

