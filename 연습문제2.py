import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5,3,1000)
y = np.random.normal(3,2,1000)

plt.scatter(x, y, color='pink', alpha=0.5)

plt.title('2021 Math Score Distribution')
plt.xlabel('score')
plt.ylabel('student')
plt.legend(['math score'], loc='upper right')
plt.show()