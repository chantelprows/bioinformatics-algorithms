import itertools

def allKmers(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))

def window(str, k):
    for i in range(1 + len(str) - k):
        yield str[i:i+k]

def hammingDistance(dna1, dna2):
    hammingDist = 0
    for i in range(len(dna1)):
        if (dna1[i] != dna2[i]):
            hammingDist += 1

    return hammingDist

def motifEnumeration(k, d, dnaList):
    patterns = []
    for kmer in allKmers(k):
        if all(any(hammingDistance(kmer, pattern) <= d
                for pattern in window(string, k)) for string in dnaList):
            patterns.append(kmer)
    return ' '.join(patterns)

DNA = ['GGGAAGAGAGTACGAACGTCAGCGG', 'CCAGTCCGGCAGCCGTGTGTTAGGC', 'AAGGGCTGAAACTCCTCCTGAGCAG', 'CTAGGAGCCGGTAGAGTATGTTGAA', 'CGCCAACGCCGAAAGAGCGGGGCAC',
'CAGTCAATACGAGGGAGCTGTTTTC', 'AGCCGTGGGTAGTTCATCGTATGTC', 'AGCAGCCCGCAGACATGAGGAGGCT', 'CGGTAACGCCCGGAAGCTTCAGCCG', 'AGCGGCCAAACTGAAATGGGGCTTC']
print(motifEnumeration(5, 1, DNA))