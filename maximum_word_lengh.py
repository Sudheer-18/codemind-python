n=input()
words=n.split(' ')
el=[]
for i in words:
    el.append(len(i))
print(max(el))