
import math   #low complexity
def prime(n):
    if n<2:
        return False
    elif n%2==0:
        return True
    elif n<=3:
        return True
    else:
        for i in range(3,int(math.sqrt(n))):
            if n%i ==0:
                return False
        return True

if __name__ =="__main__":
    n =int(input())
    if prime(n):
        print("%i is prime"%n)
    else:
        print("%i is not prime"%n)
