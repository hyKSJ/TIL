import sys
input = sys.stdin.readline

A = int(input())
B = [list(map(int,input().split())) for _ in range(A)]
B.sort()
maxH1 = 0
maxH2 = 0
C = []
D = []
sum1 = 0

for i in range(len(B)):
    if B[i][1] > maxH1:
        maxH1 = B[i][1]
        C.append([B[i][0],maxH1])

for j in range(len(B)-1,-1,-1):
    if B[j][1] > maxH2:
        maxH2 = B[j][1]
        D.append([B[j][0],maxH2])

if len(C) != 1:
    for k in range(len(C)-1):
        sum1 += C[k][1] * abs(C[k][0] - C[k+1][0])

if len(D) != 1:
    for k in range(len(D)-1):
        sum1 += D[k][1] * abs(D[k][0] - D[k+1][0])

if C[-1][0] != D[-1][0]:
        sum1 += maxH1 * (D[-1][0] - C[-1][0])

sum1 += maxH1

print(sum1)