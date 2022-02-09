import matplotlib.pyplot as plt

data1 = [500,450,520,610]
data2 = [690,700,820,900]
data3 = [1100,1030,1200,1380]
data4 = [1500,1650,1700,1850]
data5 = [1990,2020,2300,2420]
data6 = [1020,1600,2200,2550]

x = [0,1,2,3]
xlabels = ['first', 'second', 'third', 'fourth']

plt.plot(x, data1, color='blue')
plt.plot(x, data2, color='orange')
plt.plot(x, data3, color='green')
plt.plot(x, data4, color='red')
plt.plot(x, data5, color='purple')
plt.plot(x, data6, color='brown')

plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.xticks(x, xlabels)
plt.legend(['2015','2016','2017','2018','2019','2020'])

plt.show()