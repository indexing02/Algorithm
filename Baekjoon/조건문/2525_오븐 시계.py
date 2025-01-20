#훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때,
#오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

#첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

hour, minute = map(int, input().split())
take = int(input())

if minute+take < 60:
    minute = minute+take
    print(hour, minute)
else:
    t = (minute+take)//60
    hour = (hour+t) % 24
    minute = (minute+take) % 60
    print(hour, minute)

#hour, minute = map(int, input().split())
#take = int(input())

# 분에 요리 시간을 더함
#minute += take

# 시간과 분 조정
#hour = (hour + minute // 60) % 24
#minute = minute % 60

# 결과 출력
#print(hour, minute)