a=int(input())
c=0
for i in range(2,a):
    if(a%i==0):
        c=1
        break;
if(c==0):
    print("prime")
else:
    print("not a prime")