def overlap(patterns):
    k = len(patterns[0])
    dict = {}
    for pattern in patterns:
        suffix = pattern[1:]
        for pattern2 in patterns:
            prefix = pattern2[:k - 1]
            if suffix == prefix and pattern != pattern2:
                dict[pattern] = pattern2
                break

    return dict

# dnaList = []

# f = open("rosalind_ba3c.txt", "r")
# f1 = f.readlines()
# for dna in f1:
#     dnaList.append(dna.strip('\n'))
# f.close()
#
# dict = (overlap(dnaList))

# for x in dict:
#     print(x + ' -> ' + dict[x])