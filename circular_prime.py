def isprime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    if(flag==0):
        return True
    return False
n=int(input())
if(isprime(n)):
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n//=10
    if(isprime(s)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")