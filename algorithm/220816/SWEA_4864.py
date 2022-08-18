A = int(input())
  
for tc in range(1, A + 1):
    B = list(input())
    C = list(input())
    T = 0
    for i in range(len(C)-len(B)+1):
        cnt = 0
        if C[i] == B[0]:
            for j in range(len(B)):
                if C[i+j] == B[j]:
                    cnt += 1
            if cnt == len(B):
                C[i+j] = ' '
                T = 1
     
 
 
    print(f'#{tc} {T}')