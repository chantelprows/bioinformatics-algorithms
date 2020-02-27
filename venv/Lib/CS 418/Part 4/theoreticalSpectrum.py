def massOf(c):
    if c == 'G':
        return 57
    if c == 'A':
        return 71
    if c == 'S':
        return 87
    if c == 'P':
        return 97
    if c == 'V':
        return 99
    if c == 'T':
        return 101
    if c == 'C':
        return 103
    if c == 'I' or c =='L':
        return 113
    if c == 'N':
        return 114
    if c == 'D':
        return 115
    if c == 'K' or c == 'Q':
        return 128
    if c == 'E':
        return 129
    if c == 'M':
        return 131
    if c == 'H':
        return 137
    if c == 'F':
        return 147
    if c == 'R':
        return 156
    if c == 'Y':
        return 163
    if c == 'W':
        return 186

def totalMass(peptide):
    total = 0
    for c in peptide:
        total += massOf(c)
    return total

def theoreticalSpectrum(peptide):
    spectrum = [0, totalMass(peptide)]
    peptide2 = peptide + peptide

    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            subpep = peptide2[j:j + i]
            spectrum.append(totalMass(subpep))
    return sorted(spectrum)

spectrum = theoreticalSpectrum('WARQPQLEYVKTLPW')

# for int in spectrum:
#     print(int, end=" ")