def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
div=[]
for i in range(1,n+1):
    if n%i==0:
        div.append(i)
c=0
for i in div:
    if not isprime(i):
        c+=1
print(c)