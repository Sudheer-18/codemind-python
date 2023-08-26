def ispalindrome(n):
    s=0
    t=n
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    if(t==s):
        return True
    return False
    
a=int(input())
i=a
j=a
while True:
    i+=1
    if(ispalindrome(i)):
        break;
while True:
    j-=1
    if(ispalindrome(j)):
        break
d1 = i-a
d2 = a-j
if(d1>d2):
    print(j)
elif(d1<d2):
    print(i)
else:
    print(j,i)