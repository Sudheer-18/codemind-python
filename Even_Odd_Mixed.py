def odd(n):
    if(n%2==0):
        return False
    return True
def even(n):
    if(n%2!=0):
        return False
    return True
import math
n=int(input())
k=int(math.log10(n)+1)
c=0
dc=0
while(n!=0):
    r=n%10
    n//=10
    if(odd(r)):
        c+=1
    elif(even(r)):
        dc+=1
if(c==k):
    print("Odd")
elif(dc==k):
    print("Even")
else:
    print("Mixed")