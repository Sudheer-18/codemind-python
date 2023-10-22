def Contains_digit(str1):
    for i in str1:
        if i.isdigit():
            return "Yes"
    return "No"
for _ in range(int(input())):
    str1=input()
    print(Contains_digit(str1))