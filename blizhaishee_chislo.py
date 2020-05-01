def nearest(lst, target):
    return min(lst, key=lambda x: abs(x - target))
input()
List = map(int, input().split())
num = int(input())
print(nearest(List, num))
