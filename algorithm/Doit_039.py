import sys
input = sys.stdin.readline
import math

N = int(input())
max_V = 2000000

lst = [0] * (max_V+1)

def palTorF(i):
    str_i = str(i)
    s = 0
    e = len(str_i) - 1
    while s <= e:
        if str_i[s] != str_i[e]:
            return False
        else:
            s += 1
            e -= 1
    return True

for i in range(2,max_V+1):
    lst[i] = i

for i in range(2,int(math.sqrt(max_V))+1):
    if lst[i] == 0:
        continue
    for j in range(2*i,max_V+1,i):
        lst[j] = 0

for i in range(N,max_V+1):
    if lst[i] != 0 and palTorF(lst[i]):
        print(lst[i])
        break