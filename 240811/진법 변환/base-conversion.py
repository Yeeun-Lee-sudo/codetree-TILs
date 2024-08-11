n, m = input().split()
m = int(m)
n = list(n)
ans = 0 

for i in range(len(n), 0, -1):
    if ord(n[i-1]) >= 65:
        ans = ans * m + (ord(n[i-1]) - 55)
    else:
        ans = ans * m + (ord(n[i-1]) - 48)

print(ans)