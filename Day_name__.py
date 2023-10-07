def day(n):
    if n==1:
        return "Monday"
    elif(n==2):
        return "Tuesday"
    elif(n==3):
        return "Wednesday"
    elif(n==4):
        return "Thrusday"
    elif(n==5):
        return "Friday"
    elif(n==6):
        return "Saturday"
    elif(n==7):
        return "Sunday"
    else:
        return "Invalid input"
n=int(input())
print(day(n))