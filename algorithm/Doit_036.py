import sys
input = sys.stdin.readline

lst = list(input().split('-'))
result = 0


for i in range(len(lst)):
    plus_lst = lst[i].split('+')
    _sum = 0
    for j in plus_lst:
        _sum += int(j)
    if i == 0:
        result += _sum
    else:
        result -= _sum

print(result)