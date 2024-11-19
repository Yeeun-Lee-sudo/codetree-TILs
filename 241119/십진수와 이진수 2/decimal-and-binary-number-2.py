n = int(input())

def toTwo(n):
    if n==0:
        return 0
        
    ans = ""
    while(n>0):
        ans += (str)(n%2)
        n //= 2
    return ans[::-1]

def toTen(n):
    two = list(map(int, str(n)))
    ans = 0

    for i in two:
        ans = ans * 2 + i
    
    return ans

print(toTwo(toTen(n)*17))