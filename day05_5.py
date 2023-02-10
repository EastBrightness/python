# return : 함수의 결과를 활용할 수 있게 해준다.

def 절댓값더하기(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    return a+b          # return 옆에 있는 값이 사용한 곳으로 전달된다.

결과1 = 절댓값더하기(3, 7)          # 결과값인 10과 같음
결과2 = 절댓값더하기(-4, 결과1)     # 결과값인 7과 같음
print(결과2)    
print(절댓값더하기(-1, -1))

# 문제1 : 리스트에 저장된 값의 총합을 구하는 함수를 만들고 return 값을 활용하여 평균을 구해보기
lst2 = [1, 2, 3, 4, 5]

def 총합(a_lst):
    result = 0      # 함수 안에서 만든 변수는 함수가 끝나면 사라진다(지역변수)
    for i in a_lst:
        result += i
    
    return result

sum = 총합(lst2)
avg = sum/len(lst2)

print('총합은', sum)
print('평균은', avg)

# 문제2 : 입력한 갯수만큼 *을 표시하는 함수
def star(num):
    for i in range(0, int(num)):
        print('*', end='')

def star2(num=1): # 이렇게 기본값을 설정할 수 도 있는데, 이러면 star2() 하면, num은 1, 별 하나
    result = ''
    for i in range(num):
        result += '*'
    return result

num = input('별의 개수를 입력하세요 >>> ')
star(num)

s1 = star2(3)
print(s1)