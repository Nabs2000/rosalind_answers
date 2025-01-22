
def transcribing_dna_into_rna(file):
    with open(file=file, mode='r') as f:
        dna_strand = f.readline()
        return dna_strand.replace('T', 'U')
