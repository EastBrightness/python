# 제어문 중첩

# 조건문 안에서 조건문
if True:
    print('조건문1 실행')
    if True:
        print('조건문2 실행')
        print('조건문2 종료')
        if False:
            print('조건문3')
        elif False:
            print('조건문2-2-2')
        else:
            print('조건문2-2-3')
            if True:
                print('조건문2-2-3-1')
    print('조건문1 종료')

print('조건문1이 False일때 실행')
# 조건문 안에서 반복문
if True:
    print('조건문1 실행')
    for i in range(3):
        print('반복문1 을', (i+1), '번쨰 실행')            #반복 끝나면.. 밑에가 이어서 실행됨.    
    print('조건문1 종료')

# 반복문 안에서 조건문
for i in range(3):
    print('반복문1 을', (i+1), '번째 실행')
    if True:
        print('조건문1 실행')
        print('조건문1 종료')
    print('반복문1 을', (i+1), '번째 종료')

# 반복문 안에서 반복문 ( 2차원 행렬 )
for i in range(2):
    print('1A', i+1)
    print('')
    for j in range(3):
        print('2B', j+1) 
    print()

'''
1A 1

2B 1
2B 2
2B 3

1A 2

2B 1
2B 2
2B 3
'''

for i in range(1, 11):
    for j in range(1, 11):
        print(j, end=' ')
    print()

'''
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
'''

# alt 누른채로 방향키 누르면 문장전체가 위아래로 움직임.