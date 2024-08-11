n, m = input().split()
m = int(m)
n = list(n)
ans = 0 

for i in range(0, len(n)):
    if ord(n[i]) >= 65:
        ans = ans * m + (ord(n[i]) - 55)
    else:
        ans = ans * m + (ord(n[i]) - 48)
print(ans)