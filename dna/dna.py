
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
