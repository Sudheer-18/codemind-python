def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
start=int(input())
stop=int(input())
for i in range(start,stop+1):
    if(is_prime(i)):
        print(i)