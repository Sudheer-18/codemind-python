n=input()
# n = 9996
flag = 0
s = ""
for i in range(len(n)):
    if(flag == 0 and n[i]=='6'):
        s += "9"
        flag = 1
    else:
        s +=n[i]
print(s)