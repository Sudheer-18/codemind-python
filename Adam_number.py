a=int(input())
b=a*a
s=0
while(a!=0):
    r=a%10
    s=s*10+r
    a=a//10
c=s*s
x=0
while(c!=0):
    e=c%10;
    x=x*10+e
    c=c//10
if(x==b):
    print("True")
else :
    print("False")

    