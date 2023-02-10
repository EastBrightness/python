# 외부 함수를 사용하는 법 : import
# 모듈 : 부품

# import 모듈명
# import 모듈명 as 별명
# from 모듈명 import 함수명

import matplotlib.pyplot as plt # 별명
# 모듈 중에 font_manager와 rc만 가져옴
from matplotlib import font_manager, rc

font = font_manager.FontProperties(fname='gulim.ttc').get_name()
rc('font', family=font)

lst = [1, 2,3 ,4,5,6,7,8 ,9, 10] 
plt.title('분포도')     # 제목 써줘
plt.xlabel('점수')      # x축 제목
plt.ylabel('갯수')      # y축 제목
plt.hist(lst)         # 막대그래프 그려줘
plt.show()            # 보여줘

