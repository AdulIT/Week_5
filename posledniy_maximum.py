intList = list(map(int, input().split()))
maxDig = intList[0]
maxIndex = 0
for i in range(1, len(intList)):
    if intList[i] >= maxDig:
        maxIndex = i
        maxDig = intList[i]
print(maxDig, maxIndex)
