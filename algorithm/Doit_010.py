from collections import deque

N, L = map(int,input().split())
lst = list(map(int,input().split()))
min_lst = deque()

for i in range(N):
    while min_lst and min_lst[-1][0] > lst[i]:
        min_lst.pop()
    min_lst.append((lst[i],i))
    if min_lst[0][1] + L == i:
        min_lst.popleft()
    print(min_lst[0][0], end=' ')