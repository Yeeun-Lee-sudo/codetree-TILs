a, b = map(int, input().split())
n = int(input())

def toNum(n, b):
    if n==0:
        return 0
        
    ans = ""
    while(n>0):
        ans += (str)(n%b)
        n //= b
    return ans[::-1]

def toTen(n, b):
    init = list(map(int, str(n)))
    ans = 0

    for i in init:
        ans = ans * b + i
    
    return ans

print(toNum(toTen(n, a), b))