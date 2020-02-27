from collections import Counter
import theoreticalSpectrum

totalMass = theoreticalSpectrum.totalMass
massOf = theoreticalSpectrum.massOf
keys = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', "W"]

def branch(peptides):
	finalList = []
	for peptide in peptides:
		for letter in keys:
			finalList.append(peptide + letter)
	return finalList

def consistent(peptide, target):
    ccounter = Counter(peptide)
    tcounter = Counter(target)

    for mass in ccounter:
        if mass not in tcounter:
            return False
        if ccounter[mass] > tcounter[mass]:
            return False
    return True

def theoreticalSpectrum(peptide):
    spectrum = [0, totalMass(peptide)]
    peptide2 = peptide + peptide

    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            subpep = peptide2[j:j + i]
            spectrum.append(totalMass(subpep))
    return sorted(spectrum)

def linearSpectrum(peptide):
	spectrum = [0]

	for i in range(0, len(peptide)):
		for j in range(i, len(peptide)):
			subpep = peptide[i:j + 1]
			spectrum.append(totalMass(subpep))
	return sorted(spectrum)

def cyclopeptideSequencing(spectrum):
    peptides = keys
    finalList = []
    while peptides != []:
        newPeptides = []
        peptides = branch(peptides)
        for peptide in peptides:
            cspectrum = theoreticalSpectrum(peptide)
            lspectrum = linearSpectrum(peptide)
            if cspectrum == spectrum:
                finalList.append(peptide)
            elif consistent(lspectrum, spectrum):
                newPeptides.append(peptide)
        peptides = newPeptides
    return finalList

def outer(peptide):
	masses = []
	for item in peptide:
		masses.append(massOf(item))
	return '-'.join(map(str,masses))

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

finalList = cyclopeptideSequencing(inList)
print(' '.join(set(map(outer, finalList))))

