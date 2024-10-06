class Num:
    def __init__(self, index, n):
        self.index = index
        self.n = n

n = int(input())
numl = []
ip = list(map(int, input().split()))

for i in range(n):
    numl.append(Num(i+1, ip[i]))

numl.sort(key=lambda x: (x.n, x.index))
ans = [0 for i in range(n)]

for i in range(n):
    temp = ip.index(numl[i].n)
    ans[temp] = i+1
    ip[temp] = 0

print(*ans)