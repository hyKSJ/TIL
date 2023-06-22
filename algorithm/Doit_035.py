import sys
input = sys.stdin.readline

N = int(input())
case = [-1,-1]
cnt = 0

lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))

lst.sort()

for i in range(N):
    if case[1] <= lst[i][0]:
        cnt += 1
        case = lst[i]
    elif lst[i][1] <= case[1]:
        case = lst[i]

print(cnt)
