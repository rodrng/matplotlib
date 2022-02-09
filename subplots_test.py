import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [5,6,7,8]
#
# fig, ax = plt.subplots(2,2, constrained_layout=True) # figure 객체와 subplot 객체를 생성 / const머시기 자동간격조절 타이틀명 겹쳐서 씀
# ax[0][0].plot(x,y,'b^-', label = 'weight')
# ax[0][0].plot(x*3,y*2,'r0:', label = 'height')
# ax[0][0].set_title('Graph NO.1')
# ax[0][0].legend(loc='best')
# ax[0][1].plot(x,y,'r--')
# ax[0][1].set_title('Graph NO.2')
# ax[1][0].plot(x,y,'ro')
# ax[1][0].set_title('Graph NO.3')
# ax[1][1].plot(x,y,'g:')
# ax[1][1].set_title('Graph NO.4')
# plt.show()

fig, ax = plt.subplots() # 객체지향 인터페이스

ax.set_title('Mean Squared Error', pad=20)
ax.set_xlim(-3,3) # x축 범위 설정
ax.set_ylim(0,3) # y축 범위 설정
ax.set_xticks([-3,-2,-1,0,1,2,3])
ax.set_yticks([1,2,3])

x = np.linspace(-3, 3, 100) # -3~3 사이의 같은 간격으로 100개 생성
# print(x)
ax.spines['left'].set_position('center') # 왼쪽 축을 가운데로 이동
ax.spines['right'].set_visible(False) # 오른쪽 축을 숨김
ax.spines['top'].set_visible(False) # 위쪽 축을 숨김

ax.plot(x, x**2)

plt.show()