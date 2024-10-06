num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b, c, d = map(int, input().split())

def days(m, d):
    ans = 0
    for i in range(m+1):
        ans += num_of_days[i]

    return ans + d

print(days(c, d) - days(a, b))