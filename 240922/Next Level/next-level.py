class Player:
    def __init__(self, idnum = "codetree", level = 10):
        self.idnum = idnum
        self.level = level
    
    def printall(self):
        print("user", self.idnum, "lv", self.level)

p1 = Player()
i, l = input().split()
l = int(l)
p2 = Player(i, l)
p1.printall()
p2.printall()