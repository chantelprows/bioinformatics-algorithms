import eulerianPath
import eulerianCycle
import overlapGraph

createGraph = eulerianCycle.createGraph
ep = eulerianPath.eulerianPath
olg = overlapGraph.overlap

def path(path):
    return ''.join([e[0] for e in path]) + path[-1][1:]

def reconstruct(k, dnaList):
    # ov = olg(dnaList)
    # map = []
    # for x in ov:
    #     map.append(x + ' -> ' + ov[x])
    graph = createGraph(dnaList)
    fin = ep(graph)
    return path(fin)


# dnaList = [
# 'CTTA',
# 'ACCA',
# 'TACC',
# 'GGCT',
# 'GCTT',
# 'TTAC'
# ]

# dnaList = []
#
# f = open("rosalind_ba3h.txt", "r")
# f1 = f.readlines()
# for dna in f1:
#     dnaList.append(dna.strip('\n'))
# f.close()
#
# print(reconstruct(25, dnaList))