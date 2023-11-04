def majority_element(arr,n):
    for i in range(n):
        ele=-1
        c=0
        for j in range(n):
            if(arr[i]==arr[j]):
                c+=1
        if c>n//2:
            return arr[i]
    return ele
n=int(input())
arr=list(map(int,input().split()))
print(majority_element(arr,n))