A = int(input())
  
for tc in range(1,A+1):
    B = [list(input())+['']*14 for _ in range(5)]
    C = ''
    for j in range(15):
        for i in range(5):
            C += B[i][j]
     
    print(f'#{tc} {C}')