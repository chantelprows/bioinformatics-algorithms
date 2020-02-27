def BWT(text):
    cycleList = []
    textCpy = text

    for i in range(len(text)):
        cycleList.append(textCpy)
        textCpy = textCpy[1:] + textCpy[0]

    finalStr = ''
    for word in sorted(cycleList):
        finalStr += word[-1]
    return finalStr


print(BWT('ag$ac'))