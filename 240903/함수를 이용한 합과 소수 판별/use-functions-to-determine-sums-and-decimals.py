def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def isEvensum(num):
    s = 0
    while num > 0:
        s = s + (num % 10)
        num = num // 10
    if s % 2 == 0:
        return True
    else:
        return False

a, b = map(int, input().split())
ans = 0
for i in range(a, b+1):
    #print(isEvensum(i))
    if isPrime(i) and isEvensum(i):
        ans += 1

print(ans)