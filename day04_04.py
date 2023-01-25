# 문자열을 저장하는 리스트
lst = []
num = 0

# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3 : 삭제하기, 4: 전체보기

while True:
    num = int(input('1:추가, 2:수정, 3:삭제, 4:조회'))
    if num == 1:
        add_list = input('추가하고자 하는 값은?')
        lst.append(add_list)    # 값을 추가 
    elif num == 2:
        origin_list = input('수정하고자 하는 값은?')
        new_list = input('어떤 값으로?')
        origin_idx = lst.index(origin_list)
        lst[origin_idx] = new_list    # 값을 수정 ( 수정하고자 하는 값, 수정할 값 )

    elif num == 3:
        del_list = input('삭제할 값은?')
        lst.remove(del_list)    # 삭제할 값 입력
        # 그냥 값 삭제도 가능.

    elif num == 4:
        print(lst)    # 전체조회
        # for i in list:
        #   print(i)
    elif num == 0:
        print('프로그램 종료')
        break
    else:
        print('없는 번호입니다.')
    
