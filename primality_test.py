
def prime(n):   #it is actully larger complexity
    for i in range(2,n):
        if i%2 ==0:
            return False
    return False

if __name__ =="__main__":
    n =int(input())
    if prime(n):
        print("yes")
    else:
        print("no")