# 조건문 if
# if 조건식:
#     조건식이 맞으면 실행할 문장
나이 = 17
if 나이 >= 20:
    print('성인입니다.')        # 만약에
else:
    print('미성년자입니다.')    # 그밖에

# if~elif~else
# if : 조건에 맞으면 실행
# elif : 위에 조건문이 틀렸을 떄만 실행하는 조건문
# else : 조건문이 틀렸을 떄 실행할 문장.
# else : 조건이 다 틀렸을 때 실행할 ㅁ누장

# 물온도 = 
# 온도가 100도 이상이면 '기체'
# 물온도가 100도 미만이면 '액체'

물온도 = 30
if 물온도 >= 100:        # 100 이상
    print('기체')       # 0 미만
elif 물온도 < 0:
    print('고체')
elif 물온도 < 100 and 물온도 >= 0:  # 0 ~ 99
    print('액체')
else:
    print('그밖에')
