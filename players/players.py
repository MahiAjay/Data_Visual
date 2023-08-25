import matplotlib.pyplot as plt 
players = ['sachin','dhoni','rahul','kohli']
runs = [180,280,360,200]
plt.xlabel('players')
plt.ylabel('runs')

plt.title('NEWS')


#condition  list

pl1=[]
r1=[]
for i in range(len(players)):
    if runs[i] >= 200:
        pl1.append(players[i])
        r1.append(runs[i])
plt.scatter(pl1,r1,marker='*',color='red',s=120,label='star')
plt.plot(pl1,r1)
plt.bar(pl1,r1)
plt.grid(color='red')
plt.plot(pl1,r1)
plt.show()

# now creating graphs