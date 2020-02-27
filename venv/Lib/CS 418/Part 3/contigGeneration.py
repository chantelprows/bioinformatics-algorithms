from Bio import SeqIO

def contigGener(graph):
    allvalues = []
    for value in graph.values():
        for str in value:
            allvalues.append(str)

    keyList = [n for n in graph if not len(graph[n]) == allvalues.count(n) == 1]
    allPaths = []
    for key in keyList:
        i = 0
        while i < len(graph[key]):
            paths = []
            while True:
                if i >= len(graph[key]):
                    str = graph[key][-1]
                else:
                    str = graph[key][i]
                paths.append((key, str))
                count = allvalues.count(str)
                if (str not in graph) or (len(graph[str]) > 1) or (count > 1):
                    break
                else:
                    key = str
            i = i + 1
            allPaths.append(paths)

    contigs = []
    for path in allPaths:
        if len(path) == 1:
            contigs.append(path[0][0] + path[0][-1][-1])
        else:
            contig = path[0][0] + path[0][-1][-1]
            for i in range(1, len(path)):
                contig = contig + path[i][-1][-1]
            contigs.append(contig)
    return contigs

def graphMaker(dnaList):
    graph = {}
    for dna in dnaList:
        tmp = []
        for dna1 in dnaList:
            if dna[:-1] == dna1[:-1]:
                tmp.append(dna1[1:])
        graph[dna[:-1]] = tmp
    return graph


# dnaList = []
# f = open("contig.txt", "r")
# f1 = f.readlines()
# for dna in f1:
#     dnaList.append(dna.strip('\n'))
# f.close()

fasta_sequences = SeqIO.parse(open("example.data.fasta"),'fasta')
# out_file = open('output.txt', 'w')
dnalist = []
t = 0
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    dnalist.append(str(sequence))
    t = t + 1




graph = graphMaker(dnalist)
print(graph)
print('\n'.join(contigGener(graph)))
