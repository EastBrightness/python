# 내장 함수 : 파이썬 내장 함수 (파이썬 언어에서 제공하는 기능)

# eval() : 문자열 형태의 연산식을 숫자로 계산
result = eval('5+5')
print('5+5')
print(result)

# format() : 문자열로 변환
result = format(10000)
# type() : 변수의 자료형태를 알려줌
print(type(result))
print(type(123))

# str() : 문자열로 변환
str(3.14)       # '3.14'
# int() : 정수로 형변환
int('3')
# float : 실수로 형변환
float(123)      # 123.0
# list(), tupe(), set(), dict() : 형변환
lst = [1, 2, 3]
print(lst)
print(tuple(lst))

result = format(10000000, ',')  # 숫자  100단위로 끊어줌
print(result)

# max() : 리스트 중 최고값
result = max(lst)   
print(result)

# min() : 리스트 중 최소값
result = min(lst)   
print(result)

# sum() : 리스트 전체 합계
result = sum(lst)
print(result)

# len() : 리스트에 저장된 갯수
result = len(lst)
print(result)

# abs() : 절댓값
result = abs(-4)
print(result)

# pow() : 제곱승
# 10^3 (10의 3승)
result = pow(10, 3)
print(result)
# divmod() : tuple(몫, 나머지) 형태로 몫, 나머지를 알려줌 (수정 불가)
result = divmod(10, 3)
print(result)

# round() : 반올림
# 3.141592를 둘째자리까지 반올림
result = round(3.141592, 2)
print(result)
result = round(3.141592)
print(result)

# enumerate() : 반복문이랑 같이 사용됨, 리스트를 여러개의 튜플로 변형시킴
# lst = [1, 2, 3] --:> (0,1) (1,2) (2,3)
# hello = ['h', 'e', 'l', 'l', 'o'] --> (0, 'h') (1, 'e') ... 이런식으로
hello = ['h', 'e', 'l', 'l', 'o']
for item in enumerate(hello):
    print(item)

# 문제1 : pow함수를 직접 만들어보자
def 포우(num1, num2):
    result = num1
    for i in range(0, num2-1):
        result = result * num1
        
    return result

# 답안 - 오답풀이 : 초기값을 1로하면, num2번만큼 딱 됨.
def 포우1(num1, num2):
    result = 1
    for i in range(num2):
        result *= num1
    return result

result = 포우(10, 3)
print(result)
result = 포우(-2, 3)
print(result)

# range(n) : 0 ~ n-1 까지 반복 (n번 반복)
# range(n, m) : n ~ m-1 까지 반복 (m-n번 반복)
# range(n, m, x) : n ~ m-1 까지 반복을 하되, 간격을 x만큼 뛰면서 반복함. (x의 기본값 1)

for i in range(3):
    print('3번 반복', i) # i == 0, 1, 2

for i in range(1, 3):
    print('3-1번 반복', i) # 1, 2

for i in range(1, 10, 2):
    print(i) # i == 1, 3, 5, 7, 9

# sorted() : 리스트를 오름차순으로 정렬
lst = [3, 4, 1, 2, 8, 6, 9]
lst2 = sorted(lst)
sorted(lst2)
print(lst)

# 내림차순으로 정렬하려면 reverse=True 로
lst3 = sorted(lst, reverse=True)
print(lst3)

