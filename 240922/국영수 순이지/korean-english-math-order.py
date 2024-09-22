class Student:
    def __init__(self, name, kor, eng, mth):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mth = mth
    
    def printall(self):
        print(self.name, self.kor, self.eng, self.mth)

n = int(input())
ppl = []
for i in range(n):
    na, k, e, m = input().split()
    k = int(k)
    e = int(e)
    m = int(m)
    ppl.append(Student(na, k, e, m))

ppl.sort(key=lambda x: (-x.kor, -x.eng, -x.mth))

for i in ppl:
    i.printall()