from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, V = map(int,input().split())

lst = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in sorted(lst[v]):
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        data = queue.popleft()
        print(data, end=' ')
        for i in sorted(lst[data]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N+1)
DFS(V)
print()
visited = [False] * (N+1)
BFS(V)