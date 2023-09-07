def isprime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
import math
a=int(input())
k=int(math.log10(a)+1)
t=a
flag=0
while(a!=0):
    r=a%10
    a=a//10
    if(isprime(r)):
        flag+=1
if(flag==k):
    if(isprime(t)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")

