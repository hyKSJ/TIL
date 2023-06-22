import sys
input = sys.stdin.readline
import math

A,B = map(int,input().split())

N = int(math.sqrt(B))

lst = [0] * (N+1)

cnt = 0

for i in range(2,N+1):
    lst[i] = i

for i in range(2,int(math.sqrt(N))+1):
    if lst[i] == 0:
        continue
    for j in range(2*i,N+1,i):
        lst[j] = 0

for i in range(2,N+1):
    if lst[i] != 0:
        for j in range(2,100):
            if A <= lst[i]**j and lst[i]**j <= B:
                cnt += 1
            elif lst[i]**j > B:
                break

print(cnt)