from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

lst = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def BFS(a,b,cnt):
    queue = deque()
    queue.append((a,b,cnt))
    visited[a][b] = True
    while queue:
        (a, b, cnt) = queue.popleft()
        if a == N-1 and b == M-1:
            return cnt
        if 0 <= a-1 < N and not visited[a-1][b] and lst[a-1][b] != '0':
            queue.append((a-1,b,cnt+1))
            visited[a-1][b] = True
        if 0 <= b - 1 < M and not visited[a][b-1] and lst[a][b-1] != '0':
            queue.append((a,b-1,cnt+1))
            visited[a][b-1] = True
        if 0 <= a+1 < N and not visited[a+1][b] and lst[a+1][b] != '0':
            queue.append((a+1,b,cnt+1))
            visited[a + 1][b] = True
        if 0 <= b+1 < M and not visited[a][b+1] and lst[a][b+1] != '0':
            queue.append((a,b+1,cnt+1))
            visited[a][b + 1] = True

print(BFS(0,0,1))