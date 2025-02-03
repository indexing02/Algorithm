# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고,
# 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며,
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
# 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다.
# 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때,
# 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

alpha = list(input())
num = []

for i in range(len(alpha)):
    if alpha[i] in "ABC":
        num.append(2)
    elif alpha[i] in "DEF":
        num.append(3)
    elif alpha[i] in "GHI":
        num.append(4)
    elif alpha[i] in "JKL":
        num.append(5)
    elif alpha[i] in "MNO":
        num.append(6)
    elif alpha[i] in "PQRS":
        num.append(7)
    elif alpha[i] in "TUV":
        num.append(8)
    elif alpha[i] in "WXYZ":
        num.append(9)

take = sum(num) + len(num)
print(take)

