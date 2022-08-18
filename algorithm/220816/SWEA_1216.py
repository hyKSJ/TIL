for tc in range(1, 11):
    A = int(input())
    D = [list(input()) for _ in range(100)]
    T = ''
    maxV = 0
 
    for i in range(100):
        for j in range(100):
                for k in range(100-j):
                    if D[i][j] == D[i][99-k]:
                        cnt = 0
                        for t in range(100-k-j):
                            if D[i][j+t] == D[i][99-k-t]:
                                cnt += 1
                        if cnt == 100-k-j:
                            if maxV < cnt:
                                maxV = cnt
 
    for i in range(100):
        for j in range(100):
                for k in range(100-j):
                    if D[j][i] == D[99-k][i]:
                        cnt = 0
                        for t in range(100-k-j):
                            if D[j+t][i] == D[99-k-t][i]:
                                cnt += 1
                        if cnt == 100-k-j:
                            if maxV < cnt:
                                maxV = cnt
 
                          
    print(f'#{tc} {maxV}')