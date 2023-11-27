def is_fibonacci(arr):
    n = len(arr)
    
    # Check if the array has at least 3 elements
    if n < 3:
        return False
    
    for i in range(2, n):
        if arr[i] != arr[i-1] + arr[i-2]:
            return False
    
    return True

# Example usage:
n=int(input())
input_array = list(map(int,input().split()))
result = is_fibonacci(input_array)

if result:
    print("yes")
else:
    print("no")
