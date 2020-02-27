import operator
from itertools import islice

def take(n, iterable):
    return list(islice(iterable, n))

def generateConvolution(spectrum, n):
    dict = {}
    for i in range(1, len(spectrum)):
        for j in range(i):
            if spectrum[i] == spectrum[j]:
                continue
            dif = abs(spectrum[i] - spectrum[j])
            if dif in dict:
               dict[dif] += 1
            else:
                dict[dif] = 1
    sortedDict = sorted(dict.items(), key=operator.itemgetter(1))
    sortedDict = sortedDict[::-1]
    dictItems = take(n, sortedDict)
    finalList = []
    for key, value in dictItems:
        #for i in range(value):
        finalList.append(key)
    return finalList

numList = []
f = open("nums.txt", "r")
f1 = f.readlines()
for num in f1:
    numList.append(num.strip('\n'))
f.close()

numList = numList[0].split(" ")

inList = []
for item in numList:
    inList.append(int(item))

# dict = generateConvolution(inList, 0)
# for i in range(len(dict)):
#     for j in range(dict[i][1]):
#         print(str(dict[i][0]), end=" ")