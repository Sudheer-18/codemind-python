n=input()
c=0
lst=[]
for i in n:
    lst.append(i)
for i in lst:
    if i==' ':
        lst.remove(i)
print(len(lst))
    