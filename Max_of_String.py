str1=input()
lst1=[]
for i in str1:
    lst1.append(ord(i))
m=max(lst1)
print(chr(m))