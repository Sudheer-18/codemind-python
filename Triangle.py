s1,s2,s3=map(int,input().split())
if(s1==s2 and s1==s3):
    print("Equilateral triangle");
elif s1==s2 or s2==s3:
    print("Isosceles triangle");
else:
    print("Scalene triangle");