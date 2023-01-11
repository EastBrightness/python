# 정수형태의 변수는 연산이 가능함.
변수1 = 10
변수2 = 5

print(변수1 + 변수2)
print(변수1 - 변수2)
print(변수1 * 변수2)
print(변수1 / 변수2)
print(변수1 % 변수2) # 나머지 구하기

덧셈 = 변수1 + 변수2
뺄셈 = 변수1 - 변수2
곱셈 = 변수1 * 변수2
나눗셈 = 변수1 / 변수2
나머지구하기 = 변수1 % 변수2

print(덧셈)
print(뺄셈)
print(곱셈)
print(나눗셈)
print(나머지구하기)

print()
print('=============')

# 사과의 총가격 구하기
# price, count(개수) 변수 만들고, 입력받기.
price = int(input('사과 가격 : '))
count = int(input('사과 갯수 : '))
total = price * count
print('사과 가격은', total, '원 입니다.')

# 10~99 사이의 숫자를 입력받아 십의자리와 일의 자리를 알려주는 프로그램 만들기.
number = float(input('숫자는요? : '))
print('십의 자리는', int(number/10) , '일의 자리는', int(number%10))

# 드래그해서 Ctlr + / 누르면, 모두 주석처리 된다.
# ㅁㅇㄴㅇㅁㄴㅇ
# ㅁㄴㅇㄴㅁㅇㅁ

num = int(input('10~99 사이의 숫자를 입력하세요 : '))
print('십')