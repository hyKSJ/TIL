import sys
input = sys.stdin.readline
import math

M, N = map(int,input().split())
lst = [0] * (N+1)

for i in range(2,N+1):
    lst[i] = i

for i in range(2,int(math.sqrt(N))+1):
    if lst[i] == 0:
        continue
    for j in range(2*i,N+1,i):
        lst[j] = 0

for i in range(M,N+1):
    if lst[i] != 0:
        print(lst[i])