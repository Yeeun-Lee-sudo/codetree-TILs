n, b = map(int, input().split())

def toB(n, b):
    if n==0:
        return 0
        
    ans = ""
    while(n>0):
        ans += (str)(n%b)
        n //= b
    return ans[::-1]

print(toB(n, b))