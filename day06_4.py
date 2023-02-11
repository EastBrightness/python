# csv 파일 ( 구 엑셀 )
# import : 외장모듈 사용 (함수나 클래스)
import csv

def csv파일생성():
    f = open('sample.csv', 'w', newline='')
    wr = csv.writer(f)
    wr.writerow([[0, '년도', '인구'], [1, '년도', '인구']])
    f.close()

def csv파일이어쓰기():
    f = open('sample.csv', 'a', newline='')
    ad = csv.writer(f)
    ad.writerow([2, '년도', '인구'])
    f.close()

def csv파일읽기():
    f = open('sample.csv', 'r')
    rd = csv.reader(f)
    for row in rd:
        print(rd)
    f.close()

csv파일읽기()