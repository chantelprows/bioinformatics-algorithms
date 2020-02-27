def eulerianCycle(graph):
    startPosition = graph[0][0]
    curPosition = graph[0][1]
    cycle = [startPosition, curPosition]
    notIncluded = graph[1:]

    while curPosition != startPosition:
        for edge in notIncluded:
            if (curPosition == edge[0]):
                cycle.append(edge[1])
                curPosition = edge[1]
                notIncluded.remove(edge)
                break


    while len(notIncluded) != 0:
        newStart = None
        position = 0

        for i, num in enumerate(cycle):
            find = False
            for edge in notIncluded:
                if num == edge[0]:
                    newStart = edge
                    notIncluded.remove(edge)
                    position = i
                    find = True
                    break
            if find:
                break

        newStartPos = newStart[0]
        newCurPos = newStart[1]
        newCycle = [newStartPos, newCurPos]

        while newCurPos != newStartPos:
            for edge in notIncluded:
                if (newCurPos == edge[0]):
                    newCycle.append(edge[1])
                    newCurPos = edge[1]
                    notIncluded.remove(edge)
                    break

        cycle = cycle[:position] + newCycle + cycle[position + 1:]

    return cycle

def createGraph(mapList):
    patternList = []
    for map in mapList:
        items = map.split(' ')
        if ',' not in items[2]:
            patternList.append((items[0], items[2]))
        else:
            ends = items[2].split(',')
            for end in ends:
                patternList.append((items[0], end))
    return patternList

# mapList = []
# f = open("rosalind_ba3f.txt", "r")
# f1 = f.readlines()
# for dna in f1:
#     mapList.append(dna.strip('\n'))
# f.close()

# mapList = [
# '0 -> 3',
# '1 -> 0',
# '2 -> 1,6',
# '3 -> 2',
# '4 -> 2',
# '5 -> 4',
# '6 -> 5,8',
# '7 -> 9',
# '8 -> 7',
# '9 -> 6'
# ]
#
# graph = createGraph(mapList)
#
# print('->'.join(eulerianCycle(graph)))