문자열 = 'hello world, my name is python'
정수 = 314
실수 = 3.14

for i in 문자열:
    print(i, end=' ') # 글자를 한개씩 나눳 ㅓ출력한다.

i = 0
while i < len(문자열):
    print(문자열[i], end=' ')
    i += 1

# str, int, float, list, tuple, dict, set
# 리스트 : 같은 주제의 변수들을 묶음으로 보관 ( 전체 출력이 가능 )
# 지하철 3칸, [10, 15, 12]
subway1 = 10
subway2 = 15
subway3 = 12

리스트 = [10, 15, 12]
for i in 리스트:
    print(i, '명')
    

# 둘은 같은 코드인데, for 이 더 간단하다.

# 문제1 : 문자열에서 알파벳 o 의 갯수를 알려주세요

count = 0
for i in 문자열:
    if(i == 'o'):
        count += 1
print('\n o의 총 개수는', count)

# 문제 2 : 1~12월 출력하되, 입력받은 월은 skip
com = int(input('입력할 달(1~12월) >> '))
for i in range(1, 13):
    if(i == com):
        continue
    print(i, "월")

# 문제 3 : 1월~ 12월을 출력하되, 입력받은 월로부터는 출력안함
com = int(input('몇 월까지만 출력할까요? >> '))
for i in range(1, 13):
    if(i == com):
        break
    print(i, "월")

# 문제 4 : 구구단을 만들어주세요.
for i in range(1, 10):
    for j in range(2, 10):
        print(j, '*', i, '=', i*j, end='\t') # 탭 키 누르기.