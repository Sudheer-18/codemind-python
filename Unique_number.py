a=input()
arr=list(map(int,str(a)))
set1=set(arr)
if len(arr)==len(set1):
    print("Unique Number")
else:
    print("Not Unique Number")