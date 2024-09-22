class mission:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

    def printall(self):
        print("secret code :", self.code)
        print("meeting point :", self.place)
        print("time :", self.time)
    
c, p, t = input().split()
mission1 = mission(c, p, t)
mission1.printall()