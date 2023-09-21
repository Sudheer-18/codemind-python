a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    s=s+i
avg=s/a
print(f"{avg:.2f}")