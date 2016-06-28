# ChIPalign, python package for ChIP-seq files alignment and filtration

##########
# Author #
##########

For questions, comments that you should interesting for improve this pipeline, please send email to victor.gaborit2@gmail.com

################
# Presentation #
################

This pipeline is created to perform alignment and filtration of ChIP-seq datas. It's related on three existing tools : bowtie2, samtools and picard-tools.
ChIPalign is a programm that allow the user to automatically align reads and filter output with the most recommended parameters.
This pipeline is implemented in python.

##################
# Required tools #
##################

To run this pipeline, three tools are required :
 
	-bowtie2 (v2.1.0)
		from shell terminal :
		sudo apt-get install bowtie2
	-samtools (v1.3.1)
		from shell terminal :
		sudo apt-get install samtools
	-picard tools (v1.95)
		from shell terminal
		sudo apt-get install picard-tools
	python (<=v2.7)

All of this three tools must be accessible in your environment variable.

################
# Installation #
################

After installed all the required tools, got to ChIPalign directory and install it with python.
	from shell terminal:
		cd /Path/to/ChIPalign
		sudo python setup.py install
This will add to your environment variable the command ChIPalign.

#########
# Usage #
#########

from shell terminal launch :

		ChIPalign
		or
		ChIPalign -h 
		or 
		ChIPalign --help

this will print to screen the usage message :

		Usage : ChIPalign [-f <path/file.fastq(.gz)> | -1 <path/fileR1.fastq(.gz)> -2 <path/file2.fastq(.gz)>] -g <path/GenomeDirectory/prefix> [options]
		-h, --help 	: print this usage message.
		REQUIRED ARGUMENTS
		-f FILE	: full path and name of single end fastq file to analyze(must be .fastq or .fastq.gz)
		or
		-1 FILE1 -2 FILE2	: full path and name of fastq file for reads 1 (-1) and reads 2 (-2) for paired end datas to analyze(must be .fastq or .fastq.gz)
		-g GENOMEPREFIX	: full path and prefix of file containing all sequnces from reference chromosomes of genome used(without extension .fa or .fasta) (exemple : hg19_AllChr)

		OPTIONNAL ARGUMENTS
		-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files(default create a new repositorie in the current directory)
		--index	: indexing genome files, must be select if the genome have not been indewed before(defaut : OFF)
		-q INT : reads filtering according to the minimum mapping quality specified	
		-F : filter out unmapped reads
		-L FILE : remove reads mapped in coordinate files given(blacklist)
		--rmdup : remove PCR duplicates and non unique mappable reads
		--sort : sort final bam file
		--bamIndex : indexing final bam file (requiring --sort)
		--name NAME : prefix to give to output files

Check software version 

		ChIPalign --version
		ChIPalign.0.0.1


#############
# Arguments #
#############

Required arguments :

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

This pipeline will produce in a directory (depend on -o option) a unique bam file named PREFIX.bam and an indexed bam file named PREFIX.bam.bai (if --bamIndex was specified).

