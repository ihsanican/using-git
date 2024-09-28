# Week 3 and 4

## gene_finder.py
This code will read FASTA file as an input and will give a list of Open Reading Frame (ORF) sequences between start (ATG) to stop (TAA,TAG,TGA) codons. The six possible reading frames are considered.

> Command line for only one input file:

    python gene_finder.py your_FASTA_file.fna

> Command line for multiple input files (the output will automatically stored inside a new directory /ORF_output from your current directory):

    ./run.sh

## gene_finder_filter.py
This code will read FASTA file as an input and will give filtered ORF with the length more than 100 codons or 300 bases. The six possible reading frames are considered.

> Command line for multiple input files (the output will automatically stored inside a new directory /ORF_filter_output from your current directory):

    ./run_filter.sh 

##gene_finder_with_RBS.py
This code will read FASTA file as an input and will give double-filtered ORF based on the length (more or equal to 300 bases) and contain Shine-Dalgarno sequence (AGGAGG) up to 20bp upstream of the start codon.

> Command line for multiple input files (the output will automatically stored inside a new directory /RBS_output from your current directory):

    ./run_RBS.sh
