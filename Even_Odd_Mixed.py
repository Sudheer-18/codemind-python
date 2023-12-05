n=int(input())
even_cnt=odd_cnt=0
t=n
while n!=0:
    r=n%10
    if r!=0 and r%2==0:
        even_cnt+=1
    else:
        odd_cnt+=1
    n//=10
if even_cnt==len(str(t)):
    print("Even")
elif odd_cnt==len(str(t)):
    print("Odd")
else:
    print("Mixed")