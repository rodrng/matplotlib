import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0, 2, 0.2)
print(data)

# plt.plot(data, data, 'r--', data, data**2, 'b-', data, data**3, 'g:')
plt.plot(data, data, color="#FF00DD", marker="^", markersize=10)
plt.plot(data, data**2, color="lightgray", linewidth=3)
plt.plot(data, data**3, 'g:')
plt.grid(True, axis='y', linestyle=":", alpha=0.5) #격자형식
plt.xticks([0,1,2], labels=['JAN','FEB','MAR'])
plt.yticks([1,2,3,4,5], labels=['100k','200k','300k','400k','500k'])
plt.tick_params(axis='both', direction='inout', length=10, pad=20, labelsize=15) #눈금 격자 위치와 길이 등등
#axis 축을정한 direction 격자안밖 length 격자길이 pad 글자와 간격 labelsize 글자 크기
title_font = {"fontsize":20, "fontweight":"bold"} #폰트 사이즈 굵기를 title_font라는 곳에 저장 다른 이름 써도됨 ㅇㅇ 그리고 아래서 불러온다 fontdict로
plt.title("Sample Graph Title", fontdict=title_font, loc="right", pad=20) # 표 위에 타이틀명 생김


plt.show()