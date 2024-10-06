class Student:
    def __init__(self, num, h, w):
        self.num = num
        self.h = h
        self.w = w

n = int(input())
stus = []

for i in range(n):
    hei, wei = map(int, input().split())
    stus.append(Student(i+1, hei, wei))

stus.sort(key=lambda x: (-x.h, -x.w, x.num))

for i in stus:
    print(i.h, i.w, i.num)