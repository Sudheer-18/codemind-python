d,c=map(int,input().split())
a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
s=a1+a2+a3
s1=b1+b2+b3
if s>=150 and s1>=150:
    wt=s+s1+c
    wc=s+s1+d+d
    if(wt<wc):
        print("YES")
    else:
        print("NO")
elif s>=150 or s1>=150:
    wt=s+s1+c+d
    wc=s+s1+d+d
    if(wt<wc):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
