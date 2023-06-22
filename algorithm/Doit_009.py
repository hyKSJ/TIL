S,P = map(int,input().split())
lst = list(input())
A,C,G,T = map(int,input().split())
cnt_lst = [0,0,0,0]
result = 0

for i in range(P):
    if lst[i] == 'A':
        cnt_lst[0] += 1
    elif lst[i] == 'C':
        cnt_lst[1] += 1
    elif lst[i] == 'G':
        cnt_lst[2] += 1
    elif lst[i] == 'T':
        cnt_lst[3] += 1

start = 0
end = P-1

while True:
    if cnt_lst[0] >= A and cnt_lst[1] >= C and cnt_lst[2] >= G and cnt_lst[3] >= T:
        result += 1
    start += 1
    end += 1
    if end > S-1:
        break
    if lst[start-1] == 'A':
        cnt_lst[0] -= 1
    elif lst[start-1] == 'C':
        cnt_lst[1] -= 1
    elif lst[start-1] == 'G':
        cnt_lst[2] -= 1
    elif lst[start-1] == 'T':
        cnt_lst[3] -= 1
    if lst[end] == 'A':
        cnt_lst[0] += 1
    elif lst[end] == 'C':
        cnt_lst[1] += 1
    elif lst[end] == 'G':
        cnt_lst[2] += 1
    elif lst[end] == 'T':
        cnt_lst[3] += 1


print(result)