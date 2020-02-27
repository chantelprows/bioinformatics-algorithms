import networkx as nx

def pairedReads(k, d, pairList):
    graph1 = graph(pairList, k)
    length = len(graph1)
    finalGraph = nx.DiGraph(graph1)
    return eulerPath(finalGraph, length, d, k)

def graph(array, k):
    graph = {}
    for string in array:
        prefix = string[0:k-1] + string[k] + string[k+1:2*k]
        suffix = string[1:k] + string[k] + string[k+2:]
        graph[prefix] = [suffix]
    return graph

def eulerPath(G, l, d, k):
    nodes = list(G.nodes())
    for node in nodes:
        if G.in_degree(node) < G.out_degree(node):
           path = list(nx.dfs_edges(G, node))
           break
    string = path[0][0][:k-1]
    for i in range (0, len(path)):
        string += path[i][1][k-2]
    for j in range(l-k-d, len(path)):
        string += path[j][1][-1]
    return string

pairList = []

r = open('pair.txt', 'r')
d = r.readlines()
for line in d:
    s = line.replace('\n', '')
    pairList.append(s)

# print(pairedReads(30, 100, pairList))


# print(EulerPath(G))