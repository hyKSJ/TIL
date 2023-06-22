N = int(input())
_lst = []

for i in range(N):
    _lst.append(int(input()))

_lst.sort()

for i in range(N):
    print(_lst[i])