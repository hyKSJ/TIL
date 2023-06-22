import sys
input = sys.stdin.readline

N, K = map(int,input().split())
lst = []
cnt = 0

for i in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)

for i in lst:
    if i <= K:
        cnt += K//i
        K = K%i

print(cnt)