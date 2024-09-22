class person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def printall(self):
        print(self.name, self.height, self.weight)

n = int(input())
ppl = []
for i in range(n):
    na, h, w = input().split()
    h = int(h)
    w = int(w)
    ppl.append(person(na, h, w))

ppl.sort(key=lambda x: x.height)

for i in ppl:
    i.printall()