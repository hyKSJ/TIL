import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    global result
    if visited[v] == True:
        return
    else:
        result = 1
        visited[v] = True
        B.remove(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(i)

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
B = list(range(1,N+1))
sum1 = 0

for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

while B:
    result = 0
    dfs(B[0])
    sum1 += result

print(sum1)