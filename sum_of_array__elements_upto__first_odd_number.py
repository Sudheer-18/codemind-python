n=int(input())
li=list(map(int,input().split()))
el=[]
for i in li:
    if i%2!=0:
        break
    el.append(i)
print(sum(el))