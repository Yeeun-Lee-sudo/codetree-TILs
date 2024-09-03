y = int(input())

def isLeapyear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    return False

if isLeapyear(y):
    print("true")
else:
    print("false")