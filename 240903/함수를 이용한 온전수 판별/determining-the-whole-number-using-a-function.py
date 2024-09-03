def isTrue(num):
    if num % 2 == 0:
        return False
    if num % 10 == 5:
        return False
    if num % 3 == 0 and not num % 9 == 0:
        return False
    return True

a, b = map(int, input().split())
ans = 0
for i in range(a, b+1):
    if isTrue(i):
        ans += 1
    else:
        continue

print(ans)