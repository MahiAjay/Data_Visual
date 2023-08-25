import matplotlib.pyplot as plt 
#creating dataset
x=[8,12,10]
y=[6,6,16]
x1=[8,12,10]
y1=[7,7,15]
#creating   x and y axis
plt.xlabel('x')             #labelling x axis as x
plt.ylabel('y')             #labelling y axis as y
plt.title('star hi star')   #assigning title
plt.scatter(x,y,marker='*',color='black',s=120,label='star')
plt.scatter(x1,y1,marker='^',color='red',s=120,label='cone')
plt.plot(x,y)           #plt.plot is used to draw lines 
plt.plot(x1,y1)   

plt.legend(loc='upper right')         #to implement the label 
plt.grid()
plt.show()


# for help use terminal

#python
#import matpltlib.pyplot as plt
#help(plt.legend())