a=int(input())
for i in range(1,a):
    c=0
    if(i*(i+1)==a):
        c=i*(i+1)
        break;
if(c==a):
    print("YES")
else:
    print("NO")