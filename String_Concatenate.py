str1=input()
str2=input()
lst=[]
lst1=[]
for i in str1:
    lst.append(i)
for j in str2:
    lst.append(j)
for i in lst:
    lst1.append(ord(i))
lst1.sort()
for i in lst1:
    print(chr(i),end='')