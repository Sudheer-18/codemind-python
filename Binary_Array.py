n=int(input())
arrr=list(map(int,input().split()))
c=0
for i in arrr:
    if i==1 or i==0:
        c+=1
if c==n:
    print(True)
else:
    print(False)