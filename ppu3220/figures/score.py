import matplotlib.pylab as plt
import numpy as np
x = [0, 0.5, 1, 2, 3, 3.5, 4, 4.5, 5, 7.5, 8.5,9]
y = [1,2,2,3,1,2,2,2,2,1,1,0]
width = 0.5
plt.bar(x, y, width, color="pink")
plt.xlabel('score')
plt.ylabel('antall')
plt.show()