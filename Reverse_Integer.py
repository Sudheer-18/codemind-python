d=int(input())
if(d<0):
    c=d-(2*d)
    s=0
    while(c!=0):
        r=c%10
        s=s*10+r
        c=c//10
    print(s-(2*s))
else:
    s=0
    while(d!=0):
        r=d%10
        s=s*10+r
        d=d//10
    print(s)
    