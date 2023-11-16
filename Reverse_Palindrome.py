def is_palindrome(n):
    s = 0
    t = n
    while n != 0:
        r = n % 10
        s = s * 10 + r
        n //= 10
    if t == s:
        return True
    return False

def reverse_Integer(n):
    s = 0
    while n != 0:
        r = n % 10
        s = s * 10 + r
        n //= 10
    return s

n = int(input())
s = n + reverse_Integer(n)
while not is_palindrome(s):
    k = reverse_Integer(s)
    s = s + k
print(s)

