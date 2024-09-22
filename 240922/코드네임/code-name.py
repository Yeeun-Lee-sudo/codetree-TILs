class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printall(self):
        print(self.name, self.score)
    
agents = []
min = 1000
a = 0
for i in range(5):
    n, s = input().split()
    s = int(s)
    if s < min:
        min = s
        a = i
    agents.append(Agent(n, s))

agents[a].printall()