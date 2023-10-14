def unique_elements(arr):
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
    return lst
n=int(input())
arr=map(int,input().split())
result=unique_elements(arr)
for i in result:
    print(i,end=' ')
    