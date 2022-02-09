import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10,8) # 그래프 이미지 사이즈 변경

data1 = np.random.normal(0, 2, 1000) # 평균이 0, 표준편차 2인 정규분포를 가지는 데이터 1000개 추출
data2 = np.random.normal(-3, 1.5, 500) # 평균이 -3, 표준편차 1.5인 정규분포를 가지는 데이터 500개 추출
data3 = np.random.normal(1.2, 1.5, 1500)

fig, ax = plt.subplots()

ax.boxplot([data1, data2, data3])

plt.show()