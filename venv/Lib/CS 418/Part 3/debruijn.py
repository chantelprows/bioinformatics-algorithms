import kmerComp

kcomp = kmerComp.kmerComp

def debruijnK(kmers):
    kmers.sort()
    dict = {}
    finalList = []
    for kmer in kmers:
        prefix = kmer[:-1]
        dict.setdefault(prefix, [])
        dict[prefix].append(kmer[1:])
        dict[prefix] = list(dict.fromkeys(dict[prefix]))  # get rid of duplicates
    for x in dict:
        finalList.append(x + ' -> ' + ','.join(dict[x]))
    return finalList

def debruijn(k, dna):
    #kmers = kcomp(k, dna)
    kmers = dna
    return debruijnK(kmers)

dnaList = []
f = open("rosalind_ba3e.txt", "r")
f1 = f.readlines()
for dna in f1:
    dnaList.append(dna.strip('\n'))
f.close()

# print(debruijnK(dnaList))

