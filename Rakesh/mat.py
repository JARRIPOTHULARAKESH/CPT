import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[2,3,4,5,6]
plt.plot(x, y,color='red',ls=':',lw=4,marker='o',markerfacecolor='green')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.grid()  
plt.show()
