n=input()
c=0
lis=n.split(' ')
for i in lis:
    if i[0] in 'AEIOUaeiou':
        c+=1
print(c)
    