class Student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

n = int(input())
stu_l = []
for i in range(n):
    na, s1, s2, s3 = input().split()
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    stu_l.append(Student(na, s1, s2, s3))

stu_l.sort(key=lambda x: x.sub1 + x.sub2 + x.sub3) 

for s in stu_l:
    print(s.name, s.sub1, s.sub2, s.sub3)