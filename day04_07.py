import matplotlib.pyplot as plt     # 그래프 그려주는 라이브러리(부속품)

# 문제 ; 80 점 이상인 사람의 수
시험점수 = [71, 85, 77, 81, 99, 23, 55, 100, 0]
_80점이상 = []

# 시험 점수 중, 80점 이상인 사람만 _80점이상 리스트로 옮기고,.
# 2. 80점 이상 길이(갯수) 구한다.

for i in range(len(시험점수)-1):
    if(시험점수[i] >= 80):
        _80점이상.append(i)
    else:
        continue

print(len(_80점이상))

# 답안
for 개인점수 in 시험점수:
    if 개인점수 >= 80:
        _80점이상.append(개인점수)

print(_80점이상)
print(len(_80점이상), '명')

plt.title('test')
plt.xlabel('score')
plt.ylabel('person')
plt.hist(시험점수)      # 막대 그래프
plt.show()              # 그려줘