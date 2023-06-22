N = int(input())
lst = list(map(int,input().split()))
M = int(input())
find_lst = list(map(int,input().split()))

lst.sort()

for find in find_lst:
    Yn = False
    s = 0
    e = N-1
    while s <= e:
        m = (s + e)//2
        if lst[m] > find:
            e = m - 1
        elif lst[m] < find:
            s = m + 1
        else:
            Yn = True
            break
    if Yn:
        print(1)
    else:
        print(0)