def symbolToNumber(char):
    if char == 'A':
        return 0
    if char == 'C':
        return 1
    if char == 'G':
        return 2
    if char == 'T':
        return 3

def patternToNumber(dna):
    if len(dna) < 1:
        return 0
    symbol = dna[-1]
    prefix = dna[:-1]
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)

#print(patternToNumber('ATGAGCACTATACTACCGCACTACC'))