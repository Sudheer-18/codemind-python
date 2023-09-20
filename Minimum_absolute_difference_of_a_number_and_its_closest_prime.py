def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
i=n
while True:
    n+=1
    if(is_prime(n)):
        a=n
        break
while True:
    n-=1
    if(is_prime(n)):
        b=n
        break
e=abs(i-a)
f=abs(i-b)
print(min(e,f))