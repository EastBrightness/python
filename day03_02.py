# 반복문 (while, for)

# for를 사용하여 hello 3번 출력하기
for 임시변수 in range(3):
    print('hello')


# 임시변수 : while에서 i를 값으로 사용 ==> 임시변수
i = 0
while i < 3:
    print(i, '번째 Hello')
    i += 1

for j in range(3):
    print(j, '번쨰 Hello')
    
# i = 1
for i in range(1, 4):   # 1~3 Hello
    print(i, '번쨰 Hello')

# range(3) == range(0, 3)   # 0부터 2까지. 0은 생략가능.
# range(1, 4) == 1 ~ 4 전까지

for i in range(1, 13):
    print(i, '월')

# 답안
for i in range(12): # 앞에 0은 생략 : 0부터 12까지.
    print((i+1), '월')

# 7의 배수만 출력해보기
for i in range(7, 101, 7):
    print(i)

# 짝수만 출력하기
for j in range(0, 11, 2):
    print(j)

# 문제 1
'''
5
4
3
2
1
'''

# 답안
num = 5
for i in range(5):
    print(num)
    num -= 1 

for i in range(5, 0, -1):
    print(i)


# 문제 2
'''
양의 정수 1개를 입력받아서
1 부터 입력한 숫자까지 합계를 알려주는 프로그램을 만들기 

ex) 10
1 ~ 10을 모두 더해서 55
ex) 9
1 ~ 9를 모두 더해서 45
'''

# 답안
count = int(input('양의 정수 입력>>'))
sum = 0
for i in range(1, count):
    sum += i
print(sum)
# --

ans = int(input('1부터 몇까지 합계를 내볼까요? >>>'))
total = 0
for i in range(1, ans+1):
    total += i

print('합계는', total)

# 문제 3 
num1 = 1
num2 = 2
backup = 0
backup = num1
num1 = num2
num2 = backup
print(num1, num2)

