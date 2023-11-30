n=input()
wrds=n.split(' ')
el=[]
for i in wrds:
    el.append(len(i))
print(min(el))