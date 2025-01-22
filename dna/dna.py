
def counting_dna_nucleotides(file):
    with open(file, 'r') as f:
        dna_strand = f.readline()
        a, c, g, t = 0, 0, 0, 0
        for base in dna_strand:
            if base == 'A':
                a += 1
            elif base == 'C':
                c += 1
            elif base == 'G':
                g += 1
            elif base == 'T':
                t += 1
    return f'{a} {c} {g} {t}'

def complementing_a_strand_of_dna(file):
    with open(file, 'r') as f:
        mappings = {'A': 'T',
                    'T': 'A',
                    'C': 'G',
                    'G': 'C'}
        dna_strand = f.readline()
        print(dna_strand)
        # Reverse
        reversed_strand = dna_strand[::-1].replace('\n', '')
        reverse_compl = ""
        for base in reversed_strand:
            reverse_compl += mappings[base]
    return reverse_compl
