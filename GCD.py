
import math

def GCD(a,b):
    return math.gcd(a,b)

if __name__ =="__main__":
    a,b =map(int,input().split())
    print(GCD(a,b))
