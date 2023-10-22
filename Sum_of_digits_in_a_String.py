def sum_of_digits(n):
    sum=0
    for char in n:
        if char.isdigit():
            sum+=int(char)
    return sum
n=input()
result=sum_of_digits(n)
print(result)