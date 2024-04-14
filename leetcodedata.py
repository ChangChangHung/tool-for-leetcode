import os
import matplotlib.pyplot as plt
import numpy as np
try:
    os.remove("data.png")
except FileNotFoundError:
    print('There is no such a file named: data.png')

def ordinal(n: int): # Credits for Ben Davis. His profile link 'https://stackoverflow.com/users/953218/ben-davis'
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix
#get the list of all files
FileList = os.listdir('./')
for file in FileList:
    if not file.replace('.py','').isdigit():
        FileList.remove(file)
FileList.sort(key=lambda x:int(x.replace('.py','')))

x=[]# ordinal
y=[]# minute
xlabels=[]# problem number
for xlabel in FileList:
    xlabel=ordinal(int(xlabel.replace('.py','')))
    xlabels.append(xlabel)

for file in FileList:
    f=open(file,'r',encoding='utf-8')
    y.append(float(f.readline().split()[1]))
    f.close()

x=np.linspace(1,len(y),len(y))
plt.plot(x,y)
plt.xticks(x,labels=xlabels)
plt.xlabel('ordinal')
plt.ylabel('minute')
plt.savefig('data.png')
plt.show()