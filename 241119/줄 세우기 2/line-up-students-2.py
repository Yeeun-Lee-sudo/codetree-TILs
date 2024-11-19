class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

stus = []
n = int(input())

for i in range(n):
    hei, wei = input().split()
    hei = int(hei)
    wei = int(wei)
    stus.append(Student(hei, wei, i+1))

stus.sort(key=lambda x: (x.h, -x.w))
for i in stus:
    print(i.h, i.w, i.num)