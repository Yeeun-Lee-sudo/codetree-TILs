n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(n):
    if n < 0:
        return 1
    
    return (lcm(n-1) * nums[n]) // gcd(lcm(n-1), nums[n])

print(lcm(n-1))