A, B = map(int,input().split())

while A != 0:
    K = B % A
    B = A
    A = K

for i in range(B):
    print(1,end='')