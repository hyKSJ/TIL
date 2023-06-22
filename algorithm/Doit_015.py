N = int(input())

lst = []
k = 1

for i in range(N):
    lst.append(int(input()))

while N != k:
    for i in range(N-k):
        if lst[i] > lst[i+1]:
            t = lst[i]
            p = lst[i+1]
            lst[i] = p
            lst[i+1] = t
    k += 1

for i in lst:
    print(i)