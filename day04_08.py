# 튜플 tuple
# tuple = ()
# 튜플 : 추가할 수가 없음

menu = ('돈가스', '순두부', '김밥')         # 튜플은 추가가 안됨.
print(menu[0])
print(menu[1])
print(menu[3])

name1 = ''
name2 = ''
name3 = ''

name1, name2, name3 = menu
name1, name2, name3 = ('안녕하세요', 'hello', '반갑습니다.')    # 이런식으로 분할 대입도 가능하다.
print(name1, name2, name3)

print(name1, name2, name3)

# 전체 조회
print('전체 메뉴를 출력합니다:')
for i in menu:
    print(i)
