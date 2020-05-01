lst = list(map(int, input().split()))
Min = lst.index(min(lst))
Max = lst.index(max(lst))
lst[Min], lst[Max] = lst[Max], lst[Min]
print(*lst)
