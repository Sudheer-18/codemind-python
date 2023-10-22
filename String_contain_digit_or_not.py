n=input()
c=0
for char in n:
    if char.isdigit():
        c+=1
if c>0:
    print(f"Contains {c} digit")
else:
    print("Doesn't contain digit")