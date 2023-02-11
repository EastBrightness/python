# pip install scikit-learn
# 머신러닝 모듈
import sklearn
# 그래프 모듈
import matplotlib.pyplot as plt
# 수학/ 과학 계산 모듈
import numpy as np
# 다차원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression # 선형데이터

print(sklearn.__version__)

'''
머신러닝(파이썬) : 데이터(정제) -> 기계학습 -> 예측결과 -> 머신러닝별 비교 후 선정
'''
# 데이터를 가져온다 csv
원본데이터 = pd.read_csv('sample.csv', encoding='cp949')
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

print('AI예측값:', 선형기계학습.predict([[4.5]])) # 4시간 반 지나면 어느정도일까?

# 점찍기
plt.scatter(x, y, color='green')    # 원본데이터는 점으로
plt.plot(x, y_pred, color='red')    # 예측데이터는 선으로
plt.title('Corrsion rate Per Hours')    # 제목 정해줘
plt.xlabel('hours') # x축 제목 정해줘
plt.ylabel('corrsion rate') # y축 제목 정해줘
plt.show()          # 그려줘