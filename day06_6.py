import csv
# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/ 과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression # 선형데이터


def csv파일생성():
    f = open('kyobo.csv', 'w', newline='')
    ad = csv.writer(f)
    ad.writerow(['방문자수', '판매량'])
    f.close()

# csv파일생성()



# 문제 1 : 머신러닝을 사용하여, 300명이 방문했을 시의 판매량을 예측해보기.
# 데이터를 가져온다 csv
원본데이터 = pd.read_csv('kyobo.csv', encoding='cp949')
print(원본데이터.head())   # head : 잘 가져왔는지 상위 다섯개만 보기 (파라미터 안에 넣을수 있음)

# x(원인), y(결과)
x = 원본데이터.iloc[:, :-1].values  # iloc : 한 줄에 렬을 나눠서 볼 수가 있음.
# : (처음부터) :-1 (마지막 전까지 )
y = 원본데이터.iloc[:, -1].values
# [0, 1, 2]
# [[0], [1], [2]]
print(x)
print(y)

선형기계학습 = LinearRegression()
# fit을 사용하면 학습을 한다. (모델 생성)
선형기계학습.fit(x, y)

# 학습한 내용을 바탕으로 예측을 해
y_pred = 선형기계학습.predict(x)
print('예측한 y값:\n', y_pred)

print('AI예측값:', 선형기계학습.predict([[300]])) # 4시간 반 지나면 어느정도일까?

# 점찍기
plt.scatter(x, y, color='green')    # 원본데이터는 점으로
plt.plot(x, y_pred, color='red')    # 예측데이터는 선으로
plt.title('Corrsion rate Per Hours')    # 제목 정해줘
plt.xlabel('hours') # x축 제목 정해줘
plt.ylabel('corrsion rate') # y축 제목 정해줘
plt.show()          # 그려줘