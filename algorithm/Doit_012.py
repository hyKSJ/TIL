N = int(input())

lst = list(map(int,input().split()))
result_lst = [0] * N
myStack = []

for i in range(N):
    while myStack and lst[myStack[-1]] < lst[i]:
        result_lst[myStack.pop()] = lst[i]
    myStack.append(i)

while myStack:
    result_lst[myStack.pop()] = -1

for i in result_lst:
    print(i,end=" ")