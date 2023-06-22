N = int(input())
M = int(input())
lst = list(map(int,input().split()))

start = 0
end = N-1
result = 0
lst.sort()

while True:
    if lst[start] + lst[end] < M:
        start += 1
    elif lst[start] + lst[end] > M:
        end -= 1
    else:
        start += 1
        end -= 1
        result += 1
    if start >= end:
        break

print(result)
