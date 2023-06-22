import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
lst = [[1,2,3,4,5,6,7,8,9] for _ in range(10)]
result = ''
result_lst = []

def isPrime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True

def DFS(result, v):

    if isPrime(int(result + str(v))):
        result += str(v)
        if len(result) == N:
            result_lst.append(result)
            return
        else:
            for i in lst[v]:
                DFS(result,i)
    else:
        return


DFS(result, 2)
DFS(result, 3)
DFS(result, 5)
DFS(result, 7)

for i in result_lst:
    print(i)