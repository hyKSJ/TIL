import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def square(n,t):
    global sum1
    global sum2
    for i in range(0,N,n):
        for j in range(0,N,n):
            cnt1 = 0
            cnt2 = 0
            for i1 in range(n):
                for j1 in range(n):
                    if A[i+i1][j+j1] == 1:
                        cnt1 += 1
                    else:
                        cnt2 += 1
            if cnt1 == 4**(t-1):
                if n == 1:
                    sum1 += 1
                else:
                    sum1 -= 3
            if cnt2 == 4**(t-1):
                if n == 1:
                    sum2 += 1
                else:
                    sum2 -= 3
    if n == N:
        return
    square(n*2,t+1)


N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]

sum1 = 0
sum2 = 0
square(1,1)
print(sum2)
print(sum1)