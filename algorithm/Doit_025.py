import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int,input().split())

lst = [[] for _ in range(N)]
visited = [False] * N
Yn = False

for i in range(M):
    a, b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

def DFS(cnt, v):
    global Yn

    if cnt == 4:
        Yn = True
        return
    visited[v] = True
    for i in lst[v]:
        if visited[i] == False:
            DFS(cnt+1, i)
    visited[v] = False

for i in range(N):
    DFS(0,i)
    if Yn:
        break

if Yn == True:
    print(1)
else:
    print(0)