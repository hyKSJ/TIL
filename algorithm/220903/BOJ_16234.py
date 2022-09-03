import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,t):
    global k
    visited[x][y] = t
    A = deque()
    A.append((x,y))
    B = []
    B.append((x,y))
    while A:
        x,y = A.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if visited[nx][ny] == t:
                continue
            if L <= abs(graph[nx][ny]-graph[x][y]) <= R:
                A.append((nx,ny))
                B.append((nx,ny))
                visited[nx][ny] = t

    if len(B) == 1:
        k += 1
        return
    sum1 = 0
    for i,j in B:
        sum1 += graph[i][j]
    for i,j in B:
        graph[i][j] = sum1//len(B)
    return


N, L, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


t = 1
while True:
    k = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == t:
                continue
            bfs(i,j,t)
    t += 1
    if k == N*N:
        break

print(t-2)