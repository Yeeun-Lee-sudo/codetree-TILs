n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))

line.sort()
ans = 0
arr = []

def choose(cnt):
    global ans
    if cnt == n:
        ans = max(ans, len(arr))
        return

    for i in range(cnt, n):
        if not arr:
            arr.append(line[i])
            choose(i+1)
            arr.pop()
            continue
        
        x1, x2 = line[i]
        nx1, nx2 = arr[-1]
        if nx2 < x1:
            arr.append(line[i])
            choose(i+1)
            arr.pop()

    ans = max(ans, len(arr))
    return

choose(0)
print(ans)