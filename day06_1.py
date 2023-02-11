# 함수 def
# 함수의 목적 : 1. 가독성 2. 코드 재활용

# 함수 정의
def 내가만든함수1():
    print('파라미터가 없는 함수, 리턴이 없는 함수')

def 내가만든함수2(num1 num2):
    print('파라미터가 있고, 리턴은 없는 함수')
    print(num1, num2)
    지역변수 = '함수 안에서 새로 만든 변수, 매개변수와 지역변수는 함수가 끝나면 공간이 없어짐'

def 내가만든함수3(num):
    print('파라미터가 있고, 리턴이 있는 함수')
    result = abs(num)            # 입력한 값에
    return result                # 내보낸다(return) : 지역변수가 함수가 끝나면 없어지기 때문에, 외부에 값을 전달하기 위한 방법.        
    print('return 밑에 있는 코드는 작동하지 않는다. return 만나마자, 함수는 그 즉시 종료됨.') # 데드코드(절대 사용될 수 없는 코드)

    # 함수의 사용 << 함수명() >>
내가만든함수1()
내가만든함수1()
내가만든함수2(1, 2)
절댓값결과 = 내가만든함수3(-1)               # return 이 있는 함수는 일반적으로 변수로 받는 형태를 취한다.
if 내가만든함수3(-1):           # return 이 있는 함수는 변수처럼 사용한다.
    print('0이 아닙니다')

# 함수 안에 있는 코드가 모두 실행된 후, return 값이 변수값으로 사용된다.
