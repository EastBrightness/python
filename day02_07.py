# '반복문 실행' 5번 하기.

기준점 = 0
while 기준점 < 5:
    print('반복문 실행')
    기준점 += 1     # 1씩 더하기.
print('while 종료')

# 1 자신의 이름을 변수에 담고 반복문을 통해서 10번 출력해보기
i = 0
name = '임동희'
while i < 10:
    print(name, i, '번')
    i += 1
print('while 종료')

# 초기값이 반드시 0일 필요는 없다.
# 증감량이 반드시 += 1 일 필요도 없다.
# 1~12월
i = 1
while i < 3:
    print(i, '월')
    i += 1

print('==============')
i = 12
while i > 0:
    print(i, '월')
    i -= 1