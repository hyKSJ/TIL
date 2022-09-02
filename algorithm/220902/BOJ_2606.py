import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    global sum1
    if visited[v] == True:
        return
    else:
        sum1 += 1
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(i)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
sum1 = 0

for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum1-1)