
n=int(input())
m=int(input())
c=0
p=0
for i in range(n,m+1):
    c=0
    if i!=1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                c=1
                break
        if(c==0):
            p+=1
print(p)