N, M = map(int,input().split())
lst = list(map(int,input().split()))
s = 0
e = 0

for i in lst:
    if s < i:
        s = i
    e += i

while s <= e:
    m = (s+e)//2
    _sum = 0
    cnt =0
    for i in range(N):
        if _sum + lst[i] > m:
            cnt += 1
            _sum = 0
        _sum += lst[i]
    if _sum != 0:
        cnt += 1
    if cnt > M:
        s = m + 1
    else:
        e = m - 1

print(s)