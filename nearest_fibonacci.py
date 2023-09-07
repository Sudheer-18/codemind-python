n=int(input())
a=0
b=1
c=a+b
if n==0:
    print("0")
while c<=n:
    a=b
    b=c
    c=a+b
if (n-b)==(c-n):
    print(b,c)
elif (n-b)<=(c-n):
    print(b)
else:
    print(c)