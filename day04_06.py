# 파이썬 내장함수(제공기능)를 리스트에 응용

# - 파이썬 자체 함수 -

# len : 전체 갯수
# max : 최대값을 알려줌
# min : 최소값을 알려줌
# sum : 전체 합계를 알려줌.

lst = [0, 1,2 ,3,4, 5,6,7, 8, 9, 8, 7,6, 5, 4,3,2, 1]
# list. : list의, 리스트 제공함수를 쓰겠단 뜻이였고, 

# 얘네는, 리스트 제공함수가 아니라, 파이썬 자체 함수로 다루는 것.
전체갯수 = len(list)
최댓값 =- max(list)
최솟값 = min(list)
전체합계 = sum(list)
평균 = sum(list)/len(list) # 전체합계를 갯수로 나누는

print(전체갯수)
print(최댓값)
print(최솟값)
print(전체합계)
print(평균)