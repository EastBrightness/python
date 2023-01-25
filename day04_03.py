cafe_menu = []

# 카페 메뉴 이름
cafe_menu.append('아메리카노')
cafe_menu.append('카페라뗴')
cafe_menu.append('카푸치노')
cafe_menu.append('카라멜마끼아또')

print(cafe_menu)
print(cafe_menu[0])

# 데이터의 갯수를 확인하는 len
리스트의갯수 = len(cafe_menu)
print(리스트의갯수)

# 수정하기
cafe_menu[0] = '에스프레소'

# 전체 출력
for i in cafe_menu:
    print(i)
