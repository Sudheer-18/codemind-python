def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
import math
n=int(input())
k=int(math.log10(n)+1)
t=n
c=0
while(n!=0):
    r=n%10
    n=n//10
    if(isprime(r)):
        c+=1
if(c==k):
    if(isprime(t)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    
