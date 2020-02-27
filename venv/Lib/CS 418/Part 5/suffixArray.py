from functools import cmp_to_key

def suffixArray(text):
    cmp = lambda i, j: \
        [1, -1][text[i] < text[j]] if text[i] != text[j] \
        else cmp(i + 1, j + 1)

    return sorted(range(len(text)), key = cmp_to_key(cmp))

# print(suffixArray('AATCGGGTTCAATCGGGGT$'))