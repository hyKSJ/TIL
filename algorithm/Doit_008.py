N = int(input())
lst = list(map(int,input().split()))
lst.sort()
result = 0


for i in range(len(lst)):
    start = 0
    end = N-1
    while True:
        if start >= end:
            break
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        if lst[start] + lst[end] < lst[i]:
            start += 1
        elif lst[start] + lst[end] > lst[i]:
            end -= 1
        else:
            result += 1
            break
print(result)
