n=int(input())
sq = n * n
temp = n
c=0
while (temp > 0):
    c+=1
    temp=temp//10
lastdigit = (sq %(10**c))
if n==lastdigit:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")