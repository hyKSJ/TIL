import sys
input = sys.stdin.readline
import heapq

N = int(input())
lst_p = []
lst_n = []
result = 0

for i in range(N):
    a = int(input())
    if a > 1:
        heapq.heappush(lst_p,-1*a)
    elif a == 1:
        result += 1
    else:
        heapq.heappush(lst_n,a)

while len(lst_p) > 1:
    x = heapq.heappop(lst_p)
    y = heapq.heappop(lst_p)
    result += x*y

if len(lst_p) == 1:
    result -= heapq.heappop(lst_p)

while len(lst_n) > 1:
    x = heapq.heappop(lst_n)
    y = heapq.heappop(lst_n)
    result += x * y

if len(lst_n) == 1:
    result += heapq.heappop(lst_n)

print(result)