from collections import deque
import sys
input = sys.stdin.readline

def BFS(v,value):
    stop = 0
    queue = deque()
    queue.append((v,value))
    visited[v] = True
    while len(queue) != 0 and stop == 0:
        start, value = queue.popleft()
        for i in lst[start]:
            if not visited[i]:
                queue.append((i,value+1))
                if value+1 == K:
                    result.append(i)
                elif value+1 > K:
                    stop = 1
                    break
                visited[i] = True



N, M, K, X = map(int,input().split())

lst = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

for i in range(M):
    a, b = map(int,input().split())
    lst[a].append(b)

BFS(X,0)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)