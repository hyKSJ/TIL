def solution(n):
    lst = []
    result = []
    answer = ''
    lst.append(n % 3)
    if n//3 >= 1:
        lst.append(n // 3)
    n = n // 3
    while n >= 3:
        if lst:
            lst.pop()
        lst.append(n % 3)
        lst.append(n // 3)
        n = n // 3

    for i in range(len(lst) - 1, -1, -1):
        if i == 0:
            result.append(lst[i])
        if i - 1 >= 0 and lst[i - 1] != 0:
            if lst[i] == 1:
                result.append(1)
            elif lst[i] == 2:
                result.append(2)
            elif lst[i] == 4:
                result.append(4)
        elif i - 1 >= 0 and lst[i - 1] == 0:
            if lst[i] == 1:
                lst[i - 1] = 4
            elif lst[i] == 2:
                lst[i - 1] = 4
                result.append(1)
            elif lst[i] == 4:
                lst[i - 1] = 4
                result.append(2)

    for i in result:
        answer += str(i)

    return answer


print(solution(11))