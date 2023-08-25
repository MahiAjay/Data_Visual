import matplotlib.pyplot as plt
import numpy as np  
phone_names=['apple','one-plus','google','lava']
sales_world=np.array([25,34,12,54])
myexplode=[0,0,0,0.2]

#creating pie chart

plt.pie(sales_world,labels=phone_names,autopct='%1.1f%%',explode=myexplode,shadow=True)
plt.show()