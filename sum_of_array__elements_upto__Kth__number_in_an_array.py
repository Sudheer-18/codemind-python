n=int(input())
li=list(map(int,input().split()))
k=int(input())
el=[]
for i in li:
    if i==k:
        el.append(k)
        break
    el.append(i)
print(sum(el))