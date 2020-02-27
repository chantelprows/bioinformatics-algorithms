def numberToSymbol(num):
    if num == 0:
        return 'A'
    if num == 1:
        return 'C'
    if num == 2:
        return 'G'
    if num == 3:
        return 'T'

def numberToPattern(num, k):
    if k == 1:
        return numberToSymbol(num)
    prefixIndex = num // 4
    remainder = num % 4
    symbol = numberToSymbol(remainder)
    prefixPattern = numberToPattern(prefixIndex, k - 1)
    return prefixPattern + symbol

#print(numberToPattern(6881, 9))