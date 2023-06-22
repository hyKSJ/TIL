N,M = map(int,input().split())

lst = map(int,input().split())
sum_lst = []
check_lst = [0] * M
_sum = 0
result = 0

for i in lst:
    _sum += i
    sum_lst.append(_sum)

for i in range(N):
    reminder = sum_lst[i] % M
    if reminder == 0:
        result += 1
    check_lst[reminder] += 1

for i in range(M):
    if check_lst[i] > 1:
        result += (check_lst[i] *(check_lst[i]-1)//2)

print(result)