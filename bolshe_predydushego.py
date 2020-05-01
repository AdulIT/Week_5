intList = list(map(int, input().split()))
for j in range(1, len(intList)):
    if intList[j] > intList[j - 1]:
        print(intList[j], end=' ')
