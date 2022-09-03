import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def lent(n):
    if n == 0:
        return 3
    return 2*lent(n-1) + 3+n

N = int(input())

for i in range(2,30):
    if N <= lent(i):
        while i-1 != 0:
            if N <= lent(i-1):
                i -= 1
                continue
            elif lent(i-1) + 1 == N:
                print('m')
                break
            elif lent(i-1) + 1 < N <= lent(i-1) + 3 + i:
                print('o')
                break
            else:
                N -= (lent(i-1)+3+i)
                i -= 1
                continue
        if i == 1:
            if N == 1:
                print('m')
            elif N == 2:
                print('o')
            elif N == 3:
                print('o')
            elif N == 4:
                print('m')
            elif N == 5:
                print('o')
            elif N == 6:
                print('o')
            elif N == 7:
                print('o')
            elif N == 8:
                print('m')
            elif N == 9:
                print('o')
            elif N == 10:
                print('o')
            elif N == 15:
                print('o')
            elif N == 16:
                print('m')
            elif N == 17:
                print('o')
            elif N == 18:
                print('o')
            elif N == 19:
                print('m')
            elif N == 20:
                print('o')
            elif N == 21:
                print('o')
            elif N == 22:
                print('o')
            elif N == 23:
                print('m')
            elif N == 24:
                print('o')
            elif N == 25:
                print('o')
        break