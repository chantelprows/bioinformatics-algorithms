import itertools

def allKmers(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))

def hammingDistance(dna1, dna2):
    hammingDist = 0
    for i in range(len(dna1)):
        if (dna1[i] != dna2[i]):
            hammingDist += 1

    return hammingDist

def d(pattern, dnaList):
    k = len(pattern)
    distance = 0
    for dna in dnaList:
        hamming_dist = float("inf")
        for i in range(len(dna) - len(pattern)):
            substr = dna[i:i+len(pattern)]
            if hamming_dist > hammingDistance(pattern, substr):
                hamming_dist = hammingDistance(pattern, substr)
        distance = distance + hamming_dist
    return distance

def medianString(dnaList, k):
    distance = float("inf")
    for kmer in allKmers(k):
        if distance > d(kmer, dnaList):
            distance = d(kmer, dnaList)
            median = kmer
    return median

DNA = ['TCACAGCACTGAAATTGGGTGGGTTCGGCCGGTCGCCATTCA',
'GGGCGACGCTTTCAACAGGCTTAACCAACATCACAGTGAGTA',
'TCGCGATCGCGAGCGTCACACATCGAATTCTCAGAGAGGAAG',
'ATGATACGGGTCTGTGGTTCATAGGCAGGTACTCTTGTTCGG',
'TCGTCGTTTAGGAGGTGTTCAAAGGCAGCATTACCCTCTCTG',
'TAAGGGGGCACCATCTGATCACAGACGACGTTACTCCGAGTG',
'GGCCGTATCCGCTTAGATACAAGTGAATGATGATTTTCATAG',
'CCAGAGTCAAAGCTCTAAATTTTTTAGATACGGATGGACCCC',
'AGGGAAGCTGTTATTCTATCAGAGAAGCGCGAATCCCGGGGG',
'TCAGAGCGTTGTAGATTGTCGACTCCGCCATTCTAAGTCGCG'
]
print(medianString(DNA, 6))