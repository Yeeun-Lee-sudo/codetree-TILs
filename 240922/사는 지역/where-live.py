class Person:
    def __init__(self, name, add, state):
        self.name = name
        self.add = add
        self.state = state

    def printall(self):
        print("name", self.name)
        print("addr", self.add)
        print("city", self.state)

n = int(input())
p_l = []

for i in range(n):
    na, a, s = input().split()
    p_l.append(Person(na, a, s))

slow = 0
for i in range(1, n):
    if p_l[slow].name < p_l[i].name:
        slow = i

p_l[i].printall()