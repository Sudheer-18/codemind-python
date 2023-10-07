u=int(input())
s=0
if(u<200):
    b=u*1.20
elif(u>200 and u<400):
    b=u*1.50
elif(u>=400 and u<600):
    b=u*1.80
else:
    b=u*2.00
if(b>400):
    s=b*0.15+b
else:
    s=b+100;
    
print(f"{s:.2f}")

    