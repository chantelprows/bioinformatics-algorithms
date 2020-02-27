def trieConstruction(patterns):
    root = dict()
    root[0] = {}
    counter = 0
    struct = []
    for pattern in patterns:
        currDict = root[0]
        for c in pattern:
            if c in currDict:
                currDict = root[currDict[c]]
            else:
                counter += 1
                root[counter] = {}
                newNode = root[counter]
                currDict[c] = counter
                currDict = newNode
    return root


patterns = []
f = open("patterns.txt", "r")
f1 = f.readlines()
for pattern in f1:
    patterns.append(pattern.strip('\n'))
f.close()

trie = trieConstruction(patterns)
# for key, value in trie.items():
#     for key2, value2 in value.items():
#         print(str(key) + '->' + str(value2) + ':' + str(key2))
