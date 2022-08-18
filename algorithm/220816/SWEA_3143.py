A = int(input())
 
for tc in range(1, A + 1):
    B1, C1 = input().split()
    B = list(B1)
    C = list(C1)
    T = 0
    if len(B) >= len(C):
        for i in range(len(B)-len(C)+1):
            cnt = 0
            if B[i] == C[0]:
                for j in range(len(C)):
                    if B[i+j] == C[j]:
                        cnt += 1
                if cnt == len(C):
                    B[i+j] = ' '
                    T += 1
    else:
        T = 0
     
    sum1 = len(B) - (len(C)-1)*T
 
    print(f'#{tc} {sum1}')