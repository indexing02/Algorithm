# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다.
# 도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다.
# 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고,
# 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.

# 바구니의 순서를 어떻게 바꿀지 주어졌을 때,
# M번 바구니의 순서를 역순으로 만든 다음,
# 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    temp = arr[a-1:b]
    temp.reverse()
    arr[a-1:b] = temp

print(" ".join(map(str, arr)))

