def isprime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=1
            break
    if(c==0):
        return True
    return False
            
a=int(input())
flag=0
for  i in range(2,a+1):
    for j in range(2,a+1):
        if(isprime(i) and isprime(j)):
            if(i*j==a):
                print(i,j)
                flag=1
                break;
    if(flag==1):
        break;
if(flag==1):
    flag=1
else:
    c=-1
    print(c)