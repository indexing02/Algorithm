# N바이트 정수까지 저장할 수 있다고 생각 하는 정수 자료형의 이름을 출력하라
# 4바이트 마다 long 출력 해야함

n = int(input())

for i in range(4, n+1, 4):
    print("long", end=" ")
print("int")
