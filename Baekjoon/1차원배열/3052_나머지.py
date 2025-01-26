# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

arr = []
n = 0

for i in range(10):
    arr.append(int(input()) % 42)

for i in range(len(arr) - 1):
    for j in range(1 + i, len(arr)):
        if arr[i] == arr[j]:
            n += 1
            break

print(10 - n)

# arr = []
# for i in range(10):
#     a = int(input())
#     if a % 42 not in arr:
#         arr.append(a % 42)
# print(len(arr))


# arr = []
# for i in range(10):
#     a = int(input())
#     arr.append(a % 42)
# print(len(set(arr)))
