
from math import*

def LCD(a,b):

    return (a*b)//gcd(a,b)
a,b =map(int,input().split())

print(LCD(a,b))
