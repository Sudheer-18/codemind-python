def is_palindrome(str1):
    if str1[::-1]==str1:
        if len(str1)%2==0:
            return "YES EVEN"
        else:
            return "YES ODD"
    else:
        return "NO"
for _ in range(int(input())):
    str1=input()
    print(is_palindrome(str1))