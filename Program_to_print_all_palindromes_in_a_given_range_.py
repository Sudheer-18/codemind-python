def ispallindrome(n):
    s=0
    t=n
    while(n!=0):
        r=n%10
        s=s*10+r
        n//=10
    if(s==t):
        return True
    return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(ispallindrome(i)):
        print(i,end=' ');
        