# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

a = 0

for i in range(n):
    if arr[i] == v:
        a += 1

print(a)
print(arr.count(v))
