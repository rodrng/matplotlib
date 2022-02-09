import matplotlib.pyplot as plt

x = [0,1,2]
data = [100, 200, 300] #Y축 값
year = ["2019", "2020", "2021"] #X축 눈금레이블(xtick)

# plt.bar(x, data, width=0.5, color="pink", edgecolor="blue", linewidth=3, align="edge")
#width 바의 크기 줄이고 color 색 핑크로 변경 edgecolor 테두리 블루 linewidth 테두리 굵기 align 눈금이 왼쪽정렬됨
# plt.xticks(x, year)
plt.style.use('ggplot') # 그래프 스타일 지정


plt.barh(x, data, height=0.5, color="green", tick_label=year) #barh 를 써서 수평그래프 출력 tick_label 값을 넣어서 year 설정

#plt.show()
plt.savefig('data/graph2.png', dpi=200) # 저장하는 코드 data 폴더에 이름.확장자까지 dpi는 해상도