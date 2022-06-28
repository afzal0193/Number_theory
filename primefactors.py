n =int(input())    #prime factors Number theury

value = []
from  math import*
while n%2 ==0:   #even division posses.
    n = n/2
    value.append(2)

for i in range(3,int(sqrt(n))+1,2):
    while (n%i==0):
        value.append(i)

        n = n/i

if n>2:
    value.append(int(n))
print(value)


