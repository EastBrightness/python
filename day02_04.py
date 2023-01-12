# 20 이상은 성인, 14세 이상은 청소년, 14세 미만은 어린이
age = int(input('나이는 몇살입니까?'))

if age >= 20:
    print('성인')
elif age >= 14: # elif : 위에 있는 if가 틀렸다는 가정 하에 실행
    print('청소년')
elif age >= 0:
    print('어린이')
else:
    print('?')

age2 = int(input('나이는 몇살입니까?'))

if age2 <= 0:
    print('잘못 입력하셨습니다.')
elif age2 <= 7:
    print('유치원')
elif age2 <= 13:
    print('초등학교')
elif age2 <= 16:
    print('중학교')
elif age2 <= 19:
    print('고등학교')
elif age2 <= 23:
    print('대학교')
else:
    print('회사원')

