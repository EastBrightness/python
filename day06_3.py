# 외장 함수 : 파일읽고쓰기

def 파일쓰기():
    # 파일 만들고 쓰기(txt) : 이미 있으면 쓰기만함.
    f = open('sample.txt', 'w', encoding='UTF-8') # w : write. 입력하겠다, r : reade, 읽겠다.
    f.write('안녕하세요 반갑습니다 감사합니다\n')  # \n : 엔터키, 한 줄 바꾸기
    f.close()

# 파일 읽기(txt)
def 파일읽기(filepath): # 파라미터에 주소창을 넣으면, 입력해서 뚝딱 들어가게 가능
    f = open(filepath, 'r', encoding='UTF-8')
    # line = f.readline()     # 한 줄을 읽어옴
    lines = f.readlines()   # 전체를 읽음
    # print(line)
    print(lines)
    for line in lines:
        print(line, end='')
    f.close()

파일읽기('sample2.txt')

# 파일 추가쓰기(txt)
def 파일추가쓰기(filepath):
    f = open(filepath, 'a+', encoding='UTF-8') # + : 추가쓰기
    f.write('다시 만나요')
    f.close()
