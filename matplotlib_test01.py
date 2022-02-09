import matplotlib.pyplot as plt


# plt.plot([1,2,3,4],[5,6,7,8], 'r-') # x축, y축 (1,5) (2,6) (3,7) (4,8) 형식으로 그래프 출력됨
# ro는 점으로 변경됨(마커라고함) 앞에r은 색, o는 색칠된동그라미, - 솔리드선, -- 점선, : 도트선 // 추가로 색은 color="css색상" 으로도 지정가능 RGB값도 가능
# plt.plot([1,2,3,4],[5,6,7,8], linestyle=":", marker="o", color="#B70000") 이런식으로도 작성 가능하다

#맨 윗줄로 한번에 쓸 수 있는데 x,y 지정해준거임 ㅇㅇ아마도
x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x, y)

plt.xlabel('X-LABEL')
plt.ylabel('Y-LABEL')
# plt.axis([0, 10, 0, 15]) # 범위 지정 꼭 네개를 넣어줘야한다 x축 0~10 , y축 0~15 지정한거임
# plt.fill_betweenx(x[1:3], y[1:3], color='yellow', alpha=0.5) #인덱싱 번호를 넣어줘야한다 alpha값은 면적의 투명도를 설정한거임
plt.fill([1.5,1.5,3.5,3.5],[2.5,4.5,2.5,4.5], color="pink")
plt.show()
