class Student:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

stus = []

for i in range(5):
    name, hei, wei = input().split()
    hei = int(hei)
    wei = float(wei)
    stus.append(Student(name, hei, wei))

stus.sort(key=lambda x: x.name)
print("name")
for i in stus:
    print(i.name, i.h, i.w)

stus.sort(key=lambda x: -x.h)
print("\nheight")
for i in stus:
    print(i.name, i.h, i.w)