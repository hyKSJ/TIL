import sys
input = sys.stdin.readline

N = int(input())

lst = []
cnt = 0

for i in range(N):
    lst.append((int(input()),i))

sort_lst = sorted(lst)

for i in range(N):
    if cnt < sort_lst[i][1] - i:
        cnt = sort_lst[i][1] - i

print(cnt + 1)
