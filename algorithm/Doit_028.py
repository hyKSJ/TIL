from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
lst = [[] for _ in range(V+1)]
visited = [False] * (V+1)
max_value = (0,-100)

for i in range(V):
    data_lst = list(map(int,input().split()))
    for i in range(1,len(data_lst),2):
        if data_lst[i] != -1:
            lst[data_lst[0]].append((data_lst[i],data_lst[i+1]))

def BFS_find(v):
    global max_value
    queue = deque()
    queue.append((v,0))
    visited[v] = True
    while queue:
        (q,distance) = queue.popleft()
        for i in lst[q]:
            if not visited[i[0]]:
                queue.append((i[0],distance + i[1]))
                visited[i[0]] = True
                if distance + i[1] > max_value[1]:
                    max_value = (i[0],distance + i[1])


BFS_find(1)
visited = [False] * (V+1)
BFS_find(max_value[0])


print(max_value[1])