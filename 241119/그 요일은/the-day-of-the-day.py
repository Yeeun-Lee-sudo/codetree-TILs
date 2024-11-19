num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1, d1, m2, d2 = map(int, input().split())
day = input()


def whichDay(m1, d1, m2, d2, d):
    days = 0
    
    for i in range(m1, m2):
        days += num_of_days[i]
    
    days += (d2-d1)
    ans = days // 7
    if days % 7 >= d:
        ans += 1
    return ans

    

print(whichDay(m1, d1, m2, d2, week.index(day)))