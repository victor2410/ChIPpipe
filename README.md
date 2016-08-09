# ChIPpipe, python package for ChIP-seq datas analysis


## Author


For questions, comments that you should be interesting for improve this pipeline, please send email to victor.gaborit2@gmail.com


## Documentation


-> fastqc documentation : http://www.bioinformatics.babraham.ac.uk/projects/fastqc/

-> Trimmomatic documentation : http://www.usadellab.org/cms/?page=trimmomatic

-> samtools documentation : http://samtools.sourceforge.net/

-> bowtie2 documentation : http://bowtie-bio.sourceforge.net/bowtie2/index.shtml

-> picard-tools documentation : https://broadinstitute.github.io/picard/

-> python documentation : https://www.python.org/

-> spp documentation : http://compbio.med.harvard.edu/Supplements/ChIP-seq/

-> macs2 documentation : https://github.com/taoliu/MACS

-> R documentation : https://www.r-project.org/other-docs.html

-> ENCODE IDR analysis : https://sites.google.com/site/anshulkundaje/projects/idr



## Presentation


This pipeline is created to perform full analysis of ChIP-seq datas. This pipeline is only automatization of existing tools or pipelines created to perform ChIP-seq datas analysis in particular case there is no biological replicates. There are three differents programm in this pipeline :

	-> trimQual : Quality check and trimming of fastq files
	-> ChIPalign : Alignment and filtration of ChIP-seq fastq files
	-> CallPeaks : Peak Calling based on ENCODE protocol with IDR analysis (requiring replicates)
	-> CallPeaks_norep : Peak Calling related on macs2 and used when no replicates are available
	-> AnnoPeaks : Annotate ChIP-seq peaks with ChromHMM annotation file

This pipeline is implemented in python.


## Required tools


To run this pipeline, these tools are required :
 
	-fastqc (v0.10.1), required for trimQual
		from shell terminal:
		sudo apt-get install fastqc
	-Trimmomatic (v0.35) required for trimQual
		present in the folder Scripts
	-bowtie2 (v2.1.0), required for ChIPalign
		from shell terminal:
		sudo apt-get install bowtie2
	-samtools (v1.3.1), required for ChIPalign, CallPeaks and CallPeaks_norep
		from shell terminal:
		sudo apt-get install samtools
	-picard tools (v1.95), required for ChIPalign
		from shell terminal:
		sudo apt-get install picard-tools
	-spp (v1.10.1), required for CallPeaks and CallPeaks_norep
		from shell terminal:
		cd path/to/ChIPpipe/Scripts
		R CMD INSTALL spp_1.10.1.tar.gz
	-macs2 (v2.1.1), required for CallPeaks_norep
		from shell terminal:
		sudo apt-get install macs2
	-python (<=v2.7), required for all
	-R (v3.0.2), required for CallPeaks and CallPeaks_norep
		from shell terminal:
		sudo apt-get install r-base
		sudo apt-get install r-base-core
		All .r and .R scripts required are present in the folder Scripts

For fastqc, bowtie2, samtools, picard-tools, macs2, python and R, these tools must be accessible in your $PATH environment variable.


## Installation


After installed all the required tools, go to ChIPpipe directory and install it with python.

	from shell terminal:
		cd /Path/to/ChIPpipe
		sudo python setup.py install

This will add to your environment variable the command ChIPpipe.
You also need to indicate path to Rscripts in your .bashrc

	from shell terminal:
		cd $HOME
		gedit .bashrc
	Add the following line:
		export RCHIPpipe_PATH = "/fullpath/to/ChIPpipe/Scripts"
	then from shell terminal:
		source ~.bashrc


## Usage


from shell terminal launch :

		ChIPpipe
		or
		ChIPpipe -h 
		or 
		ChIPpipe --help

this will print to screen the usage message :

		usage ChIPpipe [-h] [--version]
		
		{trimQual, ChIPalign, CallPeaks, CallPeaks_norep, AnnoPeaks}

		ChIPpipe, pipeline for alignment and peak calling of ChIP-Seq datas

		POSITIONAL COMMANDS:
		trimQual	Quality check and trimming of ChIP-seq fastq
		ChIPalign	Alignment and filtration of ChIP-Seq fastq
		CallPeaks	PeakCalling based on IDR analysis protocol proposed by ENCODE (requiring biological replicates)
		CallPeaks_norep	PeakCalling when no biological replicates are available
		AnnoPeaks	Annotate ChIP-seq peaks with ChromHMM annotation file

		OPTIONAL ARGUMENTS:
			-h, --help 	: usage.
			--version : version of ChIPpipe


Check software version 

		ChIPpipe --version
			ChIPpipe.0.0.1



## Subprogramms


### trimQual:
	
	Call:

		ChIPpipe trimQual [-f FILE.fastq(.gz)> | -1 FILE_R1.fastq(.gz)> -2 FILE_R2.fastq(.gz)>] --lib INT [options]

	Required arguments:

		-f FILE	: full path and name of single end fastq file to analze (could be .fastq or .fastq.gz)
		or
		-1 FILE_R1 -2 FILE_R2	: full path and name of fastq file R1 (-1) and R2 (-2) for paired end data (could be .fastq or .fastq.gz)
		--lib INT	: select the adaptator library following used sequencer (0: Illumina Genome Analyzer IIx ; 1: Hi Seq 2000)

	Optionnal arguments:

		-o DIRECTORY	: output directory in which put all output files (default create trimQual_out in current directory)
		--adapt <PE|SE>	: Sequencing library used for adaptators (default depend on -f (SE) or -1 (PE) options)
		-h, --help 	: print this usage message

### ChIPalign:
	
	Call:

		ChIPpipe ChIPalign [-f FILE.fastq | -1 FILE_R1.fastq -2 FILE_R2.fastq] -g GENOME_PREFIX [options]

	Required arguments:

		-f FASTQ_FILE : full path and name of single end fastq file
		or
		-1 FASTQ_FILE_R1 and -2 FASTQ_FILE_R2 : full path and name of paired end R1 and R2 files
		-g GENOME_PREFIX: full path and prefix of genome reference fasta file (without '.fa' or '.fasta' extension)

	Optionnal arguments:

		-o DIRECTORY : to specify the place you want your output files in (default : create ChIPalign_out in current directory)
		--name PREFIX : prefix name to give to output files (default is fastqfile prefix)
		--index : index the reference genome (required for alignment but just need to be done once) (default : OFF)
		-q INT : filter reads with mapping quality lower than specific threshold (INT) (default : OFF)
		-F : filter unmapped reads (default : OFF)
		-L FILE : filter reads that mapp inside specific regions like blacklist regions given in specified FILE (default : OFF)
		--rmdup : filter PCR duplicates and non uniquely mapable reads (default : OFF)
		--sort : sort final bam file per reads position (default : OFF)
		--bamIndex : index final bam file (required --sort option) (default : OFF)
		-h, --help 	: usage

### CallPeaks:
	
	Call:
	
		ChIPpipe CallPeaks -1 FILE_REP1.bam -2 FILE_REP2.bam --c1 CONTROL_FILE.bam [options]
	
	Required Arguments:

		-1 FILE_REP1	: full path and name of replicate 1 file (bam file)
		-2 FILE_REP2	: full path and name of replicate 2 file (bam file)
		--c1 FILE_CONTROL	:  full path and name of control file (bam file)

	Optionnal Arguments:

		--c2 FILE_CONTROL	:  full path and name of second control file (if there is one) (bam file)
		-o DIRECTORY	: full path to directory in wich write all output files (default create a CallPeaks_out directory in the current directory)
		--idr FLOAT	: Perform IDR analysis on output peakCalling files with a specified threshold (0.01 or 0.02 for transcription factor) (default : OFF)
		--sets	: Create final peak sets (conservative and optimum) corresponding to IDR threshold (require --idr option) (default :OFF)
		--no-plots	: Do not plot IDR results (default : ON)
		--name NAME : prefix to give to output files (default is CallPeaks)
		-h, --help 	: usage


### CallPeaks_norep:

	Call:

		ChIPpipe CallPeaks_norep -f FILE.bam -c CONTROL_FILE.bam [options]
	
	Required Arguments:

		-f FILE	: full path and name of alignment file to analyze (bam format)
		-c FILE	: full path and name of Input alignment file to use (bam format)

	Optionnal Arguments:

		-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)
		--thresh STR	: pvalue threshold for peak calling (ex : 1e-7 ; default = 1e-3)
		--spp-qual	: Cross-correlation analysis performed by spp before calling peaks (default: OFF)
		--name NAME : prefix to give to output files (default is CallPeaks_macs)
		-h, --help 	: usage

### AnnoPeaks:
	
	Call:

		ChIPpipe AnnoPeaks -f <path/peakfile> -a <path/ChrommHMMannotationFile.bed> --peakCaller <spp|macs2> [options]

	Required Arguments:

		-f FILE	: full path and name of peak file 
		-a FILE	: full path and name of ChromHMM annotation file (bed file)

	Optionnal Arguments:

		-o OUTPUTDIRECTORY	: full path and name of directory in wich writes all output files (default create a new repositorie in the current directory)
		--plot	: for plotting annotation results (default is off)
		--name NAME : prefix to give to output files (default is AnnoPeaks)
		-h, --help 	: usage
	

## Output 


### trimQual :
	
	This tool will produce a folder (depend on -o option) which will contains two subfolders:

		-> One fasqtc_report folder which contains all fastQC quality check outputs
		-> One fastq_trim folder which contains all fastq files trimmed  

### ChIPalign:

	This tool will produce in a folder (depend on -o option) a unique bam file named PREFIX.bam and an indexed bam file named PREFIX.bam.bai (if --bamIndex was specified).

### CallPeaks:

	This tool will create four differents folders:

		-> One tagAlign folder which contains all file tranformed from the initial bam file (replicates, pseudo-replicates, pool, control files...) in tagAlign format
		-> One PeakCalling folder which contains all file issue from spp PeakCalling for each tagAlign file (including cross-correlation graphs)
		-> One IDR folder (if --idr options have been set) which contains all file produce by IDR analysis and one folder plots which contains all IDR graphs if --no-plots option have not been set
		-> finalsets folder (if --sets option have been set) which contains the two final peaks sets (optimum and conservative)

### CallPeaks_norep:

	This tool will generate two folders:

		-> One tagAlign folder which contains all file tranformed from the initial bam file (treatment and Input file...) in tagAlign format
		-> One PeakCalling folder which contains all file issue from macs2 PeakCalling for each tagAlign file (including cross-correlation graphs)
		
### AnnoPeaks:
	
	This tool will generate four differents bed files:
	
		-> One for all promoter and one for all enhancer region
		-> One for ChIP-seq peaks that fall into promoter region and one for peaks that fall into enhancer region

