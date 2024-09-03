m, d = map(int, input().split())

days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]

if m == 2:
    if d > 28:
        print("No")
    else:
        print("Yes")
elif m in days30:
    if d > 30:
        print("No")
    else:
        print("Yes")
elif m in days31:
    if d > 31:
        print("No")
    else:
        print("Yes")
else:
    print("No")