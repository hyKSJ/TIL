N,M = map(int,input().split())

lst = [[0]*(N+1)]
sum_lst = []
for _ in range(N+1):
    sum_lst.append([0]*(N+1))


# 값 받아두기
for i in range(N):
    lst.append([0]+list(map(int,input().split())))

# sum list 만들기
for i in range(1,N+1):
    for j in range(1,N+1):
        sum_lst[i][j] = sum_lst[i][j-1] + sum_lst[i-1][j] - sum_lst[i-1][j-1] + lst[i][j]

# 정답 계산
for i in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    result = sum_lst[x2][y2] - sum_lst[x2][y1-1] -sum_lst[x1-1][y2] + sum_lst[x1-1][y1-1]
    print(result)
