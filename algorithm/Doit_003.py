N,M = map(int,input().split())

A = map(int,input().split())
sum_lst = [0]
_sum = 0
for i in A:
    _sum += i
    sum_lst.append(_sum)


for i in range(M):
    S,E = map(int,input().split())
    print(sum_lst[E] - sum_lst[S-1])