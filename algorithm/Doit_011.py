N = int(input())
lst = [0] * N
cnt_lst = []
cnt = 1
result = []
TorF = True

for i in range(N):
    lst[i] = int(input())

for i in range(N):
    if lst[i] >= cnt:
        while lst[i] >= cnt:
            cnt_lst.append(cnt)
            cnt += 1
            result.append('+')
        cnt_lst.pop()
        result.append('-')
    else:
        n = cnt_lst.pop()
        if n > lst[i]:
            print('NO')
            TorF = False
            break
        else:
            result.append('-')

if TorF:
    for i in result:
        print(i)