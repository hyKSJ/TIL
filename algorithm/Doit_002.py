N = int(input())

A = list(map(int,(input().split())))
A.sort()
_sum = 0

for i in A:
    _sum += i


print(_sum/N/A[-1]*100)