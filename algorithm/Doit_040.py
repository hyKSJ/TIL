import sys
input = sys.stdin.readline
import math

M, N = map(int,input().split())
lst = [0] * (N+1-M)
cnt = 0

for i in range(2,int(math.sqrt(N))+1):
    go = int(M/i**2)
    if M%(i**2) !=0:
        go += 1
    for j in range(go,int(N/(i**2))+1):
        lst[int((j*i**2)-M)] = 1

for i in range(0,N+1-M):
    if lst[i] == 0:
        cnt += 1

print(cnt)