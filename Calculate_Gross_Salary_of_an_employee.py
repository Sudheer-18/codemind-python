salary=float(input())
hra=float(input())
da=float(input())
pf=salary*0.12
print(f"{pf:.2f}")
gs=salary+hra+da+pf
print(f"{gs:.2f}")