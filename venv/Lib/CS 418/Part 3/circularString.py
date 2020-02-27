import debruijn
import reconstruct
import eulerianCycle

deb = debruijn.debruijn
rec = reconstruct.reconstruct
ec = eulerianCycle.eulerianCycle
createGraph = eulerianCycle.createGraph

def path(path, k):
    return path[0][:k-1] + ''.join([e[-1] for e in path[:-k]])

def binary(k):
    return [bin(i)[2:].zfill(k) for i in range(2**k)]

def circularString(k):
    list = binary(k)
    map = deb(k, list)
    graph = createGraph(map)
    fin = ec(graph)
    return path(fin, k)


print(circularString(9))