def is_harshad(n):
    t=n
    s=0
    while n!=0:
        r=n%10
        s+=r
        n//=10
    if  t%s==0:
        return "YES"
    return "NO"
for _ in range(int(input())):
    k=int(input())
    print(is_harshad(k))