def isprime(n):
    c=0
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
for k in range(1,n+1):
    m=int(input())
    i=m
    j=m
    while True:
        if(isprime(i)):
            break
        i+=1
    while True:
        j-=1
        if(isprime(j)):
            break
    d1=0
    d2=0
    d1=i-m
    d2=m-j
    if(d1>d2):
        print(j)
    elif(d1<d2):
        print(i)
    else:
        print(j)