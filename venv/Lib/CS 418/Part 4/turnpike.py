from math import sqrt
from numpy import isnan

def setDifs(difs, d):
    difs.sort()
    difList = []
    i = 0
    for dif in difs:
        found = False
        while i < len(d):
            if d[i] < dif:
                difList.append(d[i])
            elif d[i] == dif:
                found = True
                i += 1
                break
            i += 1
        if not found:
            return None

    while i < len(d):
        difList.append(d[i])
        i += 1
    return difList

def explore(pep, x, first, last, d):
    difs = [abs(pep - i) for i in x if not isnan(i) and i != pep]
    difList = setDifs(difs, d)
    if difList == None:
        return None
    elif len(difList) == 0:
        return x
    else:
        return findPoints(x, difList, first, last)

def findPoints(x, d, first, last):
    xmax = d[-1]
    restOfx = x[:]
    restOfx[last - 1] = xmax
    final = explore(xmax, restOfx, first, last - 1, d)
    if final == None:
        restOfx = x[:]
        restOfx[first + 1] = x[-1] - xmax
        return explore(x[-1] - xmax, restOfx, first + 1, last, d)
    else:
        return final

def turnpike(numList):
    lend = len(numList)
    lenx = int(sqrt(lend))
    x = [float('nan')] * lenx
    x[0] = 0
    x[-1] = numList[-1]
    final = findPoints(x, [i for i in numList[:-1] if i > 0], 0, -1)
    return final

numList = []
f = open("nums.txt", "r")
f1 = f.readlines()
for num in f1:
    numList.append(num.strip('\n'))
f.close()

numList = numList[0].split(" ")

finalList = []
for item in numList:
    finalList.append(int(item))

tp = turnpike(finalList)
# print(*tp, end=" ")