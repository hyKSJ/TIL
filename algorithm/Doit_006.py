N = int(input())
start = 1
end = 1
_sum = 1
result = 0

while True:
    if _sum < N:
        end += 1
        _sum += end
        if start == end:
            break

    elif _sum > N:
        _sum -= start
        start += 1
        if start == end:
            break

    else:
        result += 1
        _sum -= start
        start += 1
        if start == end:
            break

if N == 1:
    print(1)
else:
    print(result+1)