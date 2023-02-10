# 머신러닝
# pip install scitkit-learn

import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

print('사이킷런 버전: ', sklearn.__version__)

# 여기서 학습을 시키고,
운동시간 = [[1], [2], [3], [4], [5]]
근육량 = [[1], [2], [3], [3.5], [3.7]]

운동시간2 = [[0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]]

lin = LinearRegression()
# 인공지능 학습 fit(x, y)
lin.fit(운동시간, 근육량)

# 학습 기반으로 예측을 함.
근육량예측 = lin.predict(운동시간)
print(근육량예측)
print('2.5시간 운동하면 근육 증가량은', lin.predict([[2.5]]))         # 2.5 시간 운동하면 근육량ㅇ ㅣ얼마일지?

plt.scatter(운동시간, 근육량예측, color='blue')         # 점
plt.plot(운동시간, 근육량, color='green')       # 선
plt.show()

