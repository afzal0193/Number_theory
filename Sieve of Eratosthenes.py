

from math import*

n =int(input())+1
list = [0]*n

for i in range(2,int(sqrt(n)),1):
    for j in range(i*i,n,i):
        list[j]  = 1

for i in range(2,len(list)):
    if list[i]==0:
        print(i)
