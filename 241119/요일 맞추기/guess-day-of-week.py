num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())

def whichDay(m1, d1, m2, d2):
    ans = 0
    rev = False

    if m1>m2:
        m1, m2 = m2, m1
        d1, d2 = d2, d1
        rev = True
    elif m1 == m2 and d1 > d2:
        d1, d2 = d2, d1
        rev = True
    
    for i in range(m1, m2):
        ans += num_of_days[i]
    
    ans += (d2-d1)

    ans %= 7
    if rev:
        ans = 7 - ans

    if ans==0:
        return "Mon"
    elif ans==1:
        return "Tue"
    elif ans==2:
        return "Wed"
    elif ans==3:
        return "Thu"
    elif ans==4:
        return "Fri"
    elif ans==5:
        return "sat"
    else:
        return "Sun"

print(whichDay(m1, d1, m2, d2))