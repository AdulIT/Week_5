elements = list(map(int, input().split()))
for i in range(1, len(elements), 2):
    elements[i - 1], elements[i] = elements[i], elements[i - 1]
print(*elements)
