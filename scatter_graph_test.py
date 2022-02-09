import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50) #0~1사이의 값들 중 임의의 50개 추출
y = np.random.rand(50)

colors = np.random.rand(50)
area = (30*np.random.rand(50))**2

plt.scatter(x,y, c=colors, s=area, alpha=0.5)
plt.show()