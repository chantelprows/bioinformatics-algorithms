def getDifChars(char):
    if char == 'A':
        return ['C', 'G', 'T']
    if char == 'C':
        return ['A', 'G', 'T']
    if char == 'G':
        return ['A', 'C', 'T']
    if char == 'T':
        return ['A', 'C', 'G']

def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighborhood = []
    suffixNeighbors = neighbors(pattern[1:], d)
    for text in suffixNeighbors:
        if hammingDistance(pattern[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                neighborhood.append(x + text)
        else:
            neighborhood.append(pattern[0] + text)

    return neighborhood

def hammingDistance(dna1, dna2):
    hammingDist = 0
    for i in range(len(dna1)):
        if (dna1[i] != dna2[i]):
            hammingDist += 1

    return hammingDist

#print('\n'.join(neighbors('ACGAAGGGCTC', 2)))