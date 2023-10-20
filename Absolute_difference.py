def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
arr=list(map(int,input().split()))
non_prime=[]
prime=[]
for i in arr:
    if(isprime(i)):
        prime.append(i)
    else:
        non_prime.append(i)
p=1
dp=1
for  i in prime:
    p*=i
for j in non_prime:
    dp*=j
print(abs(p-dp))
    
        