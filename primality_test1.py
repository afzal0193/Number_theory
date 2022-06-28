
import math
def prime(n):  #sqrt complexity
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
if __name__ =="__main__":
    n =int(input())
    if prime(n):
        print("yes")
    else:
        print("no")

