def isprime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=1
            break
    if(c==0):
        return True
    return False
def ispalindrome(n):
    t=n
    s=0
    while(n!=0):
       r=n%10
       s=s*10+r
       n=n//10
    if(s==t):
        return True
    return False
a=int(input())
i=a
while True:
    i+=1
    if(ispalindrome(i)):
        if(isprime(i)):
            break;
print(i)