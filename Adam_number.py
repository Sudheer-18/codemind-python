n=int(input())  ##12
sq=n*n  ##144
s=0
while n!=0:
    r=n%10
    s=s*10+r   ##21
    n//=10
qs=s*s        ##441

s1=0
while qs!=0:
    r=qs%10
    s1=s1*10+r   ##144
    qs//=10
    
if s1==sq:
    print("True")
else:
    print("False")
    