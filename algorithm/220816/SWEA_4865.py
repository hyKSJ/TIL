A = int(input())
 
for tc in range(1, A+1):
    B = input()
    C = input()
    maxV = 0
 
    B1 = set(B)
    for i in B1:
        cnt = 0
        for j in C:
            if i == j:
                cnt += 1
        if cnt > maxV:
            maxV = cnt
 
 
    print(f'#{tc} {maxV}')