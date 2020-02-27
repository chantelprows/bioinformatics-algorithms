def numPeptides(mass):
    i = mass
    weights = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    ways = [0]*(mass + 1)
    ways[i] = 1
    while i > 0:
        for weight in weights:
            ways[i - weight] += ways[i]
        i = i - 1
        while ways[i] == 0:
            i = i - 1

    return ways[0]

print(numPeptides(1397))