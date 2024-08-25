def tf(n):
    if n%3==0:
        return True
    else:
        while True:
            if n % 10 == 3 or n%10 == 6 or n%10 == 9:
                return True
            n = n // 10
            if n == 0:
                return False

def count(a, b):
    ans = 0
    for i in range(a, b+1):
        if tf(i):
            ans += 1
    return ans

a, b = map(int, input().split())
print(count(a, b))