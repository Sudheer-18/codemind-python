def result(n):
    k=n[::-1]
    if k==n:
        return 'Palindrome'
    return 'Not Palindrome'
n=input()
print(result(n))