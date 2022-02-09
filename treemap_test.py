import matplotlib.pyplot as plt
import squarify

sizes = [40,30,20,10]

labels = ['apple', 'orange', 'banana', 'grape']
colors = ['red', 'blue', 'green', 'yellow']

squarify.plot(sizes, 10, 10, label=labels, color=colors)



plt.show()