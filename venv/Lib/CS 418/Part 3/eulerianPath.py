import eulerianCycle

createGraph = eulerianCycle.createGraph
eulerianCycle = eulerianCycle.eulerianCycle

def eulerianPath(graph):
    bal = balance(graph)
    graph.append(bal)
    ep = eulerianCycle(graph)
    del ep[-1]

    for i in range(len(ep) - 1):
        if (ep[i] == bal[0] and ep[i + 1] == bal[1]):
            end = ep[i + 1:]
            front = ep[:i + 1]
            # print('->'.join(end + front))
            return end + front


def balance(graph):
    dictKeys = {}
    dictValues = {}
    for edge in graph:
        dictKeys.setdefault(edge[0], 0)
        dictKeys[edge[0]] = dictKeys[edge[0]] + 1
        dictValues.setdefault(edge[1], 0)
        dictValues[edge[1]] = dictValues[edge[1]] + 1

    max = len(dictKeys)
    if (len(dictValues) > max):
        max = len(dictValues)

    key = None
    value = None
    for i in range(max):
        ikey = list(dictKeys.keys())[i]
        ivalue = list(dictValues.keys())[i]
        # if (str(id) not in dictKeys and str(id) not in dictValues):
        #         #     continue
        skip = False
        if ivalue not in dictKeys:
            key = ivalue
            skip = True
        if ikey not in dictValues:
            value = ikey
            skip = True
        if skip == False:
            if dictKeys[ikey] != dictValues[ikey]:
                if dictKeys[ikey] > dictValues[ikey]:
                    value = ikey
                elif dictValues[ikey] > dictKeys[ikey]:
                    key = ikey
            if dictKeys[ivalue] != dictValues[ivalue]:
                if dictKeys[ivalue] > dictValues[ivalue]:
                    value = ivalue
                elif dictValues[ivalue] > dictKeys[ivalue]:
                    key = ivalue
        if key != None and value != None:
            break

    return(key, value)

# mapList = []
# f = open("rosalind_ba3g.txt", "r")
# f1 = f.readlines()
# for dna in f1:
#     mapList.append(dna.strip('\n'))
# f.close()

# mapList = [
# '0 -> 2',
# '1 -> 3',
# '2 -> 1',
# '3 -> 0,4',
# '6 -> 3,7',
# '7 -> 8',
# '8 -> 9',
# '9 -> 6'
# ]

# graph = createGraph(mapList)
# eulerianPath(graph)

