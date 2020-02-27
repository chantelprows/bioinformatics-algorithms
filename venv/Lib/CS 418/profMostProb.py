from functools import reduce

def mostProbable(dna, k, matrix):
    best_pattern = ""
    best_probability = 0
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i + k]
        if calculate_probablity(kmer, matrix) > best_probability:
            best_pattern = kmer
            best_probability = calculate_probablity(kmer, matrix)
    return best_pattern

def calculate_probablity(kmer, matrix):
    prob = []
    for i in range(len(kmer)):
        if kmer[i] == 'A':
            prob.append(matrix[0][i])
        elif kmer[i] == 'C':
            prob.append(matrix[1][i])
        elif kmer[i] == 'G':
            prob.append(matrix[2][i])
        elif kmer[i] == 'T':
            prob.append(matrix[3][i])
    return reduce((lambda x, y: x * y), prob)

print(mostProbable('ACGACGCGTTTGACAGAGCAGAAGGGCCTTCGGACGCTGCACTAAATCCGTTTATCATCATTCCACCACCGTTCGAGAATGACCCGTGCCCTGGCCACGCTCTGCGTGACCGGCTAATTCCAAATGGTCTCTAGGATCCGAATTAACGGGCTTGCGAAGTGTAATAACTCACACCAGTGCCGACCTCCGTAATCGGGAGG', 8,
[[0.16, 0.36, 0.24, 0.24, 0.24, 0.24, 0.32, 0.28],
[0.28, 0.28, 0.28, 0.2, 0.28, 0.2, 0.36, 0.2],
[0.16, 0.2, 0.28, 0.36, 0.28, 0.32, 0.12, 0.32],
[0.4, 0.16, 0.2, 0.2, 0.2, 0.24, 0.2, 0.2]]))