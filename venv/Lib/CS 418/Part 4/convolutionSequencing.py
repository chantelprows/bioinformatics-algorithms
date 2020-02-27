import generateConvolution
import itertools
import leaderboard
import heapq
from collections import Counter

genCon = generateConvolution.generateConvolution
cut = leaderboard.cut
genS = leaderboard.generate_subspectrums
score = leaderboard.score

def select_spectrum(Spectrum,M):
    poten = [pt1-pt2 for pt1,pt2 in itertools.product(Spectrum,Spectrum) if pt1-pt2 >= 57 and pt1-pt2 <= 200]
    lst = Counter(poten).most_common()
    tie = heapq.nlargest(M,lst,key=lambda x:x[1])[-1][1]
    res = list(filter(lambda x: x[1]>=tie, lst))
    return list(zip(*res))[0]

def leaderboard(spectrum, m, n):
    weights = select_spectrum(spectrum, m)
    leaderboard = [0]
    leaderPeptide = []
    while True:
        leaderboard = [list(pep) for pep in itertools.product(leaderboard, weights)]
        for peptide in leaderboard:
            try:
                exSpectrum = genS(peptide)
            except:
                leaderboard = [peptide[0] + [peptide[1]] if x == peptide else x for x in leaderboard]
                peptide = peptide[0] + [peptide[1]]
                exSpectrum = genS(peptide)

            if max(exSpectrum) == max(spectrum):
                lexSpectrum = genS(leaderPeptide)
                if score(spectrum, exSpectrum) > score(spectrum, lexSpectrum):
                    leaderPeptide = peptide
            elif max(exSpectrum) > max(spectrum):
                leaderboard.remove(peptide)
        leaderboard = cut(leaderboard, spectrum, n)
        if leaderboard == []:
            break
    return leaderPeptide

def convolutionSequencing(m, n, spectrum):
    lb = leaderboard(spectrum, m, n)
    lb.remove(0)
    return lb

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

cs = convolutionSequencing(20, 370, finalList)
print(*cs, sep='-')