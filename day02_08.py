# 1. 횟수입력받아서 그 수만큼 Hello 출력하는 프로그램

count = int(input('몇 번 출력하시겠습니까?'))
i = 1

while i < count:
    print(i, '번째 Hello')
    i += 1

# 1 답안-

i = 0

while i < count:
    i += 1
    print(i, '번쨰 Hello')

# 2. 1 ~100 사이에서 7의 배수만 출력하는 프로그램 ( while 안에서 if 를 사용 )

i = 1

while(1 <= i <= 100):
    if(i % 7 == 0):
        print('7의 배수입니다.', i)
        i += 1
    else:
        i += 1

# 3. 커피 자판기 : 커피 1잔에 300원, 금액을 입력하여 총 몇잔의 커피와 잔돈이 얼마나 남는지 출력하시오.
# 금액은 얼마인가요 >> 1400원
# 커피 1잔, 잔돈 100원. 이런 식으로.

cost = int(input(' 금액은 얼마인가요 >> '))
coffee = 300
i = 1
cup = int(cost/coffee)

while(cost - coffee * i >= 0): # 잔돈이 0원보다 큰 경우엔,
    print('커피', i, '잔, 잔돈', cost - coffee * i)
    i += 1

# 컵을 1잔씩 늘리기. while -> 잔돈이 300원 이하일 때까지.
# 잔돈 계산해야하니, cost - coffe * i