def mins(day, hour, m):
    ans = (day-11)*24*60+(hour-11)*60+(m-11)
    if ans < 0:
        return -1
    else:
        return ans

a, b, c = map(int, input().split())
print(mins(a, b, c))