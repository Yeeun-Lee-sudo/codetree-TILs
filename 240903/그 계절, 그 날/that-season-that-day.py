y, m, d = map(int, input().split())
days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]

def isLeapyear(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    return False

def dayExist(y, m, d):
    if m in days31:
        return True
    elif m in days30:
        if d == 31:
            return False
        else:
            return True
    else: 
        if isLeapyear(y):
            if d > 29:
                return False
            else:
                return True
        else:
            if d > 28:
                return False
            else:
                return True

if dayExist(y, m, d):
    if m == 3 or m == 4 or m == 5:
        print("Spring")
    elif m == 6 or m == 7 or m == 8:
        print("Summer")
    elif m == 9 or m == 10 or m == 11:
        print("Fall")
    elif m == 12 or m == 1 or m == 2:
        print("Winter")
else:
    print("-1")