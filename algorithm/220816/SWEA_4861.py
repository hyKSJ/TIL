A = int(input())
 
for tc in range(1, A + 1):
    B, C = map(int, input().split())
    D = [list(input()) for _ in range(B)]
    T = ''
 
    for i in range(B):
        for j in range(B - C + 1):
            cnt = 0
            if C % 2:
                for k in range(C//2+1):
                    if D[i][j + k] == D[i][j + C - 1 - k]:
                        cnt += 1
                if cnt == C // 2 + 1:
                    for t in range(C):
                        T += D[i][j + t]
            else:
                for k in range(C//2):
                    if D[i][j + k] == D[i][j + C - 1 - k]:
                        cnt += 1
                if cnt == C // 2:
                    for t in range(C):
                        T += D[i][j + t]
 
    for i in range(B):
        for j in range(B - C + 1):
            cnt = 0
            if C % 2:
                for k in range(C//2+1):
                    if D[j+k][i] == D[j + C - 1 - k][i]:
                        cnt += 1
                if cnt == C // 2 + 1:
                    for t in range(C):
                        T += D[j + t][i]
            else:
                for k in range(C//2):
                    if D[j + k][i] == D[j + C - 1 - k][i]:
                        cnt += 1
                if cnt == C // 2:
                    for t in range(C):
                        T += D[j + t][i]
                         
    print(f'#{tc} {T}')