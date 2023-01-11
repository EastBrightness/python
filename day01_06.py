# 연산자
a = 10
b = 3

a + b # 덧셈 13 
a - b # 뺄셈 7
a * b # 곱셈 30
a / b # 나눗셈 3.3 
a % b # 나머지구하기 연산자 1
a ** b # a 의 b 제곱

a = b # b 값을 a 공간 에 대입한다.
a == b # 같다 (수학의 = )
a != b # 다르다
a > b # a 가 크다 
a < b # a 가 작다
a >= b # a가 b보다 크거나 같다
a <= b # a가 b보다 작거나 같다

# 대입연산자 '=' 주의할 점 = 
a = a # 왼쪽은 공간의 개념의 a이고, 오른쪽은 a 안에 들어갈 값이다.
  
# 줄임말
a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a /= b # a = a / b

(a + b) * a # 곱셈 연산자가 + 보다 빠르다. 우선순위를 위해선 ( ) 로 감싸주면 그거 먼저함.

# 비교 연산자 == , >=, >
a = 10
b = 3
print(a != b) # 10은 3과 다르냐? => true(다르다)
print(a == b) # 10은 3과 같냐? => false(다르다)
print(a > b) # 10 > 3 --> True

# 관계연산자 and, or, not
print(a > 5 and a < 15) # a 는 5보다 크고 15보다 작다. ( 둘다 true여야 true 반환. ) => true

# a는 0보다 작거나, 5보다 크다. ( 둘 중에 하나만 true여도 true 반환. ) => ture
print(a < 0 or a > 5) # True

# and : 둘 다 맞아야만 맞고, 나머지는 다 틀림.
# or : 둘 중 하나만 맞아도 맞다.

print(a < 0 and a > 5) # a는 0보다 작지 않아서 False
print(a < 0 or a > 100) # 둘 다 틀려서 False.
print(not b == 3 ) # not 키워드 : Fals는 True로, True는 False로

