import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

lst.sort()
sum = 0
final_sum = 0
for i in lst:
    sum += i
    final_sum += sum

print(final_sum)