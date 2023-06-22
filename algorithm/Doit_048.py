import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
    global stop
    queue = deque()
    queue.append(v)
    visited[v] = 'red'
    while queue:
        start = queue.popleft()
        for i in lst[start]:
            if visited[i] == visited[start]:
                print('NO')
                queue = []
                stop = True
                break
            if visited[i] == False:
                if visited[start] == 'red':
                    visited[i] = 'blue'
                else:
                    visited[i] = 'red'
                queue.append(i)

T = int(input())

for i in range(T):
    V, E = map(int,input().split())
    lst = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for j in range(E):
        u,v = map(int,input().split())
        lst[u].append(v)
        lst[v].append(u)
    stop = False

    for i in range(1,V+1):
        if visited[i] == False:
            BFS(i)
        if stop == True:
            break
    if not stop:
        print('YES')

