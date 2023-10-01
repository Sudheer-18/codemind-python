import math
n=int(input())
c=0
arr=list(map(int,input().split()))
for i in arr:
    k=int(math.log10(i)+1)
    if(k%2==0):
        c+=1
print(c)
    