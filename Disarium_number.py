import math
n=int(input())
t=n
s=0
k=int(math.log10(n)+1)
for i in range(k,0,-1):
    r=n%10
    s=s+int(r**i)
    n//=10
if(s==t):
    print("True")
else:
    print("False")