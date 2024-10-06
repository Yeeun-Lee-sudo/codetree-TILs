class Student:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

stus = []
n = int(input())

for i in range(n):
    name, hei, wei = input().split()
    hei = int(hei)
    wei = int(wei)
    stus.append(Student(name, hei, wei))

stus.sort(key=lambda x: (x.h, -x.w))
for i in stus:
    print(i.name, i.h, i.w)