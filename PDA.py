n=int(input())
s=0
str=""
for i in range(1,n):
    if n%i==0:
        s+=i
if s<n:
    str+="DEFICIENT";
elif s==n:
    str+="PERFECT";
else:
    str+="ABUNDANT";
print(str)
    