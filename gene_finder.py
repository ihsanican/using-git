def gene_finder(file):
	record = list(SeqIO.parse(file,"fasta"))
	genome = ""
	for i in range(len(record)):
		genome += record[i].seq
	N = len(genome)

	return None
