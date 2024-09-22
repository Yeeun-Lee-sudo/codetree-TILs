class Rainyday:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
    
    def printall(self):
        print(self.date, self.day, self.weather)

n = int(input())
dates = []
for i in range(n):
    date, day, weather = input().split()
    dates.append(Rainyday(date, day, weather))

rain = []
for i in range(n):
    if dates[i].weather == "Rain":
        rain.append(dates[i])

fastest = rain[0]
for i in range(len(rain)):
    if int(fastest.date[:4]) > int(rain[i].date[:4]):
        fastest = rain[i]
    elif int(fastest.date[:4]) == int(rain[i].date[:4]):
        if int(fastest.date[5:7]) > int(rain[i].date[5:7]):
            fastest = rain[i]
        elif int(fastest.date[5:7]) == int(rain[i].date[5:7]):
            if int(fastest.date[8:]) > int(rain[i].date[8:]):
                fastest = rain[i]

fastest.printall()