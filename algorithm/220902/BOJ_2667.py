def dfs(x,y):
    global cnt
    if x<0 or x>N-1 or y<0 or y>N-1:
        return
    if A[x][y] == 1:
        cnt += 1
        A[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return


N = int(input())

A = [list(map(int,input())) for _ in range(N)]
B = []
result = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(i,j) == True:
            result += 1
            B.append(cnt)

print(result)
B.sort()
for i in B:
    print(i)