T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    _mul = A * B
    while A != 0:
        K = B % A
        B = A
        A = K
    print(_mul//B)
