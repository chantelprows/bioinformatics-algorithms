import random
import copy

def randomizedMotifSearch(dna, k, t):
    best_motifs = []
    for i in range(t):
        rand = random.randrange(len(dna[0]) - k)
        best_motifs.append(dna[i][rand:rand + k])
        final_motifs = best_motifs
    while True:
        prof = profilepc(final_motifs)
        motifs = []
        for i in range(len(dna)):
            motifs.append(profileMostProbablePattern(dna[i], k, prof))
        final_motifs = motifs
        if score(final_motifs) < score(best_motifs):
            best_motifs = final_motifs
        else:
            return best_motifs

def profilepc(motifs):
    cnt = count(motifs)
    profile = {}
    for letter in cnt.keys():
        profile[letter] = [float(x + 1) / (len(motifs) + 4) for x in cnt[letter]]
    return profile

def profileMostProbablePattern(text, k, profile):
    p_dict = {}
    for i in range(len(text) - k + 1):
        p = pr(text[i:i+k], profile)
        p_dict[i] = p
    m = max(p_dict.values())
    keys = [k for k,v in p_dict.items() if v == m]
    ind = keys[0]
    return text[ind:ind+k]

def pr(text, profile):
    p = 1
    for i in range(len(text)):
        p = p * profile[text[i]][i]
    return p

def score(motifs):
    con = consensus(motifs)
    score = 0
    for i in range(len(motifs[0])):
        freq_sym = con[i]
        for j in range(len(motifs)):
            if motifs[j][i] != freq_sym:
                score = score + 1
    return score

def consensus(motifs):
  counter = count(motifs)
  consensus = ""
  for j in range(len(motifs[0])):
      m = 0
      frequentSymbol = ""
      for symbol in "ACGT":
          if counter[symbol][j] > m:
              m = counter[symbol][j]
              frequentSymbol = symbol
      consensus += frequentSymbol
  return consensus


def count(motifs):
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(len(motifs[0])):
            count[symbol].append(0)

    for i in range(len(motifs)):
        for j in range(len(motifs[0])):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    return count

def repeatedRandomizedMotifSearch(dna, k, t):
    best_score = float('inf')
    best_motifs = []
    for i in range(1000):
        motifs = randomizedMotifSearch(dna, k, t)
        curScore = score(motifs)
        if curScore < best_score:
            best_score = curScore
            best_motifs = motifs
    return '\n'.join(best_motifs)


