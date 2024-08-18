n, m = map(int, input().split())
ans = []

def choose(cnt):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(cnt, n+1):
        ans.append(i)
        choose(i+1)
        ans.pop()
    return

choose(1)