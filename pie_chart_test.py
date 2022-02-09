import matplotlib.pyplot as plt

data = [34, 32, 16, 18]
label = ["A","B","C","D"]
explode = [0,0.1,0,0.1]
colors = ['silver','gold','whitesmoke','lightgray']

plt.pie(data, labels=label, autopct="%.1f%%", startangle=90, counterclock=False,
        explode=explode, shadow=True, colors=colors)
plt.show()