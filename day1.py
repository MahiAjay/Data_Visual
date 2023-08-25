import matplotlib.pyplot as plt
import time
#checking list of functions under plt
for i in dir(plt):  #dir of anythingis a list
   if 'F' in i: 
    print(i)
#    time.sleep(1)    #take second as number argument    
    
    
    #right way
x1 = [i for i in dir(plt) if 'F' in i]
print(x1)      