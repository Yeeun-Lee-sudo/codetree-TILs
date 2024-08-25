n, m = map(int, input().split())

def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n

print(gcd(n, m))