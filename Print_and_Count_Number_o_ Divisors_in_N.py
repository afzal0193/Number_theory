


"""find divisor by  O(sqrt)complexcity """
n =int(input())
s = set()
for i in range(1,int(n**0.5)+1):
    if (n%i==0):
        x = i
        y = n//i
        s.add(x)
        s.add(y)

print(len(s))

