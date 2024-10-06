class Pos:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

n = int(input())
poss = []

for i in range(n):
    x, y = map(int, input().split())
    poss.append(Pos(i+1, x, y))

poss.sort(key=lambda x: (abs(x.x) + abs(x.y), x.num))
for i in poss:
    print(i.num)