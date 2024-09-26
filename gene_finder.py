from Bio import SeqIO

def gene_finder(file):
	record = list(SeqIO.parse(file,"fasta"))
	genome = ""
	for i in range(len(record)):
		genome += record[i].seq
	N = len(genome)

	start_codon = "ATG"
	stop_codons = ["TAA","TAG","TGA"]
	amino_acids = []

	for i in range(3): # run for three reading frames
		stop = False
		idx1,idx2 = 0,i
		while stop==False:
			for j in range(idx2,N,3):
				if j>=(N-3):
					stop=True
					break
				if seq[j:j+3]==start_codon:
					idx1=j
					break
			for j in range(idx1+3,N,3):
				if j>=(N-3):
					stop=True
					break
				if seq[j:j+3] in stop_codons:
					idx2=j
					if seq[idx1:idx1+3]==start_codon:
						amino_acids.append(seq[idx1:idx2+3])
					break
			idx2=idx1+3

	return amino_acids
