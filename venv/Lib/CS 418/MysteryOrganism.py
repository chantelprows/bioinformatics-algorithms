from Bio import SeqIO
import itertools
import Ros6
import Ros3
import Ros7
import Ros11
import Ros9
import Ros10
import Ros8

minimumSkew = Ros6.minimumSkew
reverseComp = Ros3.reverseComp
hammingDist = Ros7.hammingDistance
neighbors = Ros11.neighbors
patternToNumber = Ros9.patternToNumber
numberToPattern = Ros10.numberToPattern
approxPatternCount = Ros8.approxPattern

def FrequentWordsWithMisAndRev(sequence, k, d):
    min_skews = minimumSkew(sequence)
    index = int(min_skews.split(' ', 1)[0])
    new_sequence = sequence[index:index + 400]

    frequent_patterns = []
    close = []
    freq_arr = []
    for i in range(4**k - 1):
        close.append(0)
        freq_arr.append(0)
    for i in range(len(new_sequence) - k):
        neighborhood = neighbors(new_sequence[i:i+k], d)
        for pattern in neighborhood:
            index = patternToNumber(pattern)
            close[index - 1] = 1
    for i in range(4**k - 1):
        if close[i] == 1:
            pattern = numberToPattern(i, k)
            freq_arr[i] = approxPatternCount(pattern, new_sequence, d)
            freq_arr[i] += approxPatternCount(reverseComp(pattern), new_sequence, d)
    maxCount = max(freq_arr)

    for i in range(4**k - 1):
        if (freq_arr[i] == maxCount):
            pattern = numberToPattern(i, k)
            frequent_patterns.append(pattern)

    return ' '.join(frequent_patterns)

fasta_sequences = SeqIO.parse(open("notSoSpooky.fasta"),'fasta')
out_file = open('output.txt', 'w')
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)
    out_file.write(str(FrequentWordsWithMisAndRev(sequence, 9, 1)))
out_file.close()

