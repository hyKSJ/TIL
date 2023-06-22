import sys
input = sys.stdin.readline
import heapq

N = int(input())
lst = []


for i in range(N):
    heapq.heappush(lst,int(input()))

if N == 1:
    print(0)
elif N == 2:
    print(lst[0] + lst[1])
else:
    result = 0
    while len(lst) != 1:
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        result += (a+b)
        heapq.heappush(lst,a+b)
    print(result)