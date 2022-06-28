
""""
Binary exponentiation Number theury এর ধারনা ..
আমারা যখন কোন সংখ্।র পওয়ার বের করি তখন আমাদের O(power) complexcty তে অপারেশন
করতে হয় যেমন :
     2^9
     এখানে power = 9 এবং Base = 2 তাহলে আমরা অপারেশন চালাতে পারি :

     result = 1
     for i in range(power):
         result = result*base
     print(result)

     উপরের এই অপারেশনটি O(power) এ কাজ করবে যার complexcty অনেক বেশি
     এই complexty কমানোর সহজ উপায় Binary exponentitiation এটা নিচের মত কাজ করে
     থাকে
     result             base               power
       1                  2                  9
       2                  2                  8
       2                  4                  4
       2                  16                 2
       2                  256                1
       512                256                0
    অপারেশন এর কোড এবং তার বিবরণ নিচে দেওয়া হলো
    এখানে যদি power বেজোর হয় তাহলে result = result * base হরে বেস এর কোন পরিবর্ত
    হবে না ও power এর মান 1 করে কমে যাবে । আবার যদি power জোড় হয় তাহলে base = base*base এবং power = power //2
    হবে উপরের অপারেশনটি চলতে থাকবে যতখন না power এর মান 0 হছে । কোডটি নিছে দেওয়া হলো

"""
#Binary exponentition code .....

base = int(input())
power = int(input())
result = 1
while power !=0:
    if power%2==1:
        power = power - 1
        result = result * base
    if power % 2==0:
        base = base * base
        power = power //2
print(result)


