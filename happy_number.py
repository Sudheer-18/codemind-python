def ishappynumber(n):
    while True:
        if(n==1 or n==7):
            return True
        elif(n<10):
            return False
        s=0
        while(n!=0):
            r=n%10
            s=s+(r*r)
            n=n//10
        n=s
n=int(input())
if(ishappynumber(n)):
    print("True")
else:
    print("False")