import matplotlib.pyplot as plt
import numpy as np

# weight = [68,71,62,77,80,71,62,68,77,65,69,78,77,75,76,69,66,65,64,63,61,80,60,69,77]
#
# plt.hist(weight)
# plt.show()

data1 = np.random.randn(10000) # 표준정규분포 임의의 데이터 10000개 추출(n은 정규분포)

font1 = {"family":"Arial",
         "color":"red",
         "weight":"bold",
         "size":15,
         "alpha":0.7
         }

plt.hist(data1, bins=100, histtype="step", density=True)
plt.text(1.0,0.1,'weight', fontdict=font1, rotation=-60)
plt.show()
