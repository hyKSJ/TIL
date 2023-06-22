N = int(input())
lst = [[] for _ in range(N)]
visited = [False] * N
result = [0] * N
lcm = 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def DFS(v):
    visited[v] = True
    for i in lst[v]:
        next = i[0]
        if not visited[next]:
            result[next] = result[v] * i[2]//i[1]
            DFS(next)

for i in range(N-1):
    a,b,p,q = map(int,input().split())
    lst[a].append((b,p,q))
    lst[b].append((a,q,p))
    lcm *= (p*q//gcd(p,q))

result[0] = lcm
DFS(0)
mgcd = result[0]

for i in range(1,N):
    mgcd = gcd(mgcd,result[i])

for i in range(N):
    print(int(result[i]//mgcd),end=' ')