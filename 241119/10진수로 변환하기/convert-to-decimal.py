def toTen(n):
    two = list(map(int, str(n)))
    ans = 0

    for i in two:
        ans = ans * 2 + i
    
    return ans

num = input()
print(toTen(num))