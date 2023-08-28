def isprime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=1
            break
    if(c==0):
        return True
    else:
        return False
a=int(input())
flag=0
for i in range(2,a+1):
    if(isprime(i)):
        for j in range(2,a+1):
            if(isprime(j)):
                if(i*j==a):
                    flag=1
                    c=i
                    c2=j
                    break;
if(flag==1):
    print(c2,c)
else:
    print("-1")