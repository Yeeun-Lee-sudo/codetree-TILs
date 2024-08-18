n, m = map(int, input().split())
r = list(map(int, input().split()))
l = []
ans = 0

def choose(cnt):
    global ans
    if len(l) == m:
        calc = l[0]
        for i in range(1, m):
            calc = calc ^ l[i]
        ans = max(ans, calc)
        return
    
    for i in range(cnt, n):
        l.append(r[i])
        choose(i+1)
        l.pop()
    return


choose(0)
print(ans)