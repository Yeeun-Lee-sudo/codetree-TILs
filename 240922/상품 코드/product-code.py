class product:
    def __init__(self, name = "codetree", code = "50"):
        self.name = name
        self.code = code

    def printall(self):
        print("product", self.code, "is", self.name)

n, c = input().split()
p1 = product()
p2 = product(n, c)
p1.printall()
p2.printall()