import theoreticalSpectrum
import heapq
import itertools
from collections import Counter

totalMass = theoreticalSpectrum.totalMass

def generate_subspectrums(peptide):
    length = len(peptide)
    looped = peptide + peptide
    return [0, sum(peptide)] + [sum(looped[start:start + length]) for start, length in itertools.product(range(0, length), range(1, length))]

def score(spectrum, exSpectrum):
    return len(list((Counter(spectrum) & Counter(exSpectrum)).elements()))

def cut(leaderboard, spectrum, n):
    if len(leaderboard) > n:
        results = []
        for peptide in leaderboard:
            try:
                exSpectrum = generate_subspectrums(peptide)
            except:
                peptide = peptide[0] + [peptide[1]]
                exSpectrum = generate_subspectrums(peptide)
            results.append((peptide, score(spectrum, exSpectrum)))
        tie = heapq.nlargest(n, results, key=lambda x: x[1])[-1][1]
        res = list(filter(lambda x: x[1]>=tie, results))
        return list(zip(*res))[0]
    else:
        return leaderboard

def leaderboard(spectrum, n):
    weights = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    leaderboard = [0]
    leaderPeptide = []
    while leaderboard != []:
        leaderboard = [list(pep) for pep in itertools.product(leaderboard,weights)]
        for peptide in leaderboard:
            try:
                exSpectrum = generate_subspectrums(peptide)
            except:
                leaderboard = [peptide[0] + [peptide[1]] if x == peptide else x for x in leaderboard]
                peptide = peptide[0] + [peptide[1]]
                exSpectrum = generate_subspectrums(peptide)

            if max(exSpectrum) == max(spectrum):
                lexSpectrum = generate_subspectrums(leaderPeptide)
                if score(spectrum, exSpectrum) > score(spectrum, lexSpectrum):
                    leaderPeptide = peptide
            elif max(exSpectrum) > max(spectrum):
                leaderboard.remove(peptide)
        leaderboard = cut(leaderboard, spectrum, n)
    return leaderPeptide

# numList = []
# f = open("nums.txt", "r")
# f1 = f.readlines()
# for num in f1:
#     numList.append(num.strip('\n'))
# f.close()
#
# numList = numList[0].split(" ")
#
# finalList = []
# for item in numList:
#     finalList.append(int(item))

# lb = leaderboard(finalList, 354)
# lb.remove(0)

# print(*lb, sep='-')