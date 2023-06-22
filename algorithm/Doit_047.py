import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        start = queue.popleft()
        for i in lst[start]:
            if not visited[i]:
                visited[i] = True
                result_lst[i] += 1
                queue.append(i)

N, M = map(int,input().split())
lst = [[] for _ in range(N+1)]
result_lst = [0] * (N+1)

for i in range(M):
    A, B = map(int,input().split())
    lst[A].append(B)

for i in range(1,N+1):
    visited = [False] * (N+1)
    BFS(i)

max_value = 0
for i in range(1,N+1):
    max_value = max(max_value, result_lst[i])

for i in range(1,N+1):
    if max_value == result_lst[i]:
        print(i, end=' ')