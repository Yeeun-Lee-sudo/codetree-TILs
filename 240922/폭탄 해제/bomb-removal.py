class bomb:
    def __init__(self, code, colour, sec):
        self.code = code
        self.colour = colour
        self.sec = sec

    def printall(self):
        print("code :", self.code)
        print("color :", self.colour)
        print("second :", self.sec)
    
c, l, s = input().split()
b1 = bomb(c, l, s)
b1.printall()