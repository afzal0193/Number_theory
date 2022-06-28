
from math import*

n =int(input())
value =[]

for i in range(2,n,1):

    if n%i ==0:
        count = 0
        while n%i ==0:
            count = count  + 1
            n = n/i
        value.append(i)

print(value)





