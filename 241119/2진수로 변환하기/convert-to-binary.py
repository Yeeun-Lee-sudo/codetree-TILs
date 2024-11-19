n = int(input())

def to2(n):
    if n==0:
        return 0
        
    ans = ""
    while(n>0):
        ans += (str)(n%2)
        n //= 2
    return ans[::-1]

print(to2(n))