a=int(input())
s=0
for i in range(a):
    b=int(input())
    s=0
    org=b
    while b!=0:
        r=b%10
        s=s*10+r
        b=b//10
    if(s==org):
        print("True")
    else :
        print("False")
    