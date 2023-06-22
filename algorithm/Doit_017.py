import sys
input = sys.stdin.readline

lst = list(input())


for i in range(len(lst)):
    Max = i
    for j in range(i+1,len(lst)):
        if lst[j] > lst[Max]:
            Max = j
    if lst[i] < lst[Max]:
        t = lst[i]
        lst[i] = lst[Max]
        lst[Max] = t

for i in range(len(lst)):
    print(lst[i],end="")
