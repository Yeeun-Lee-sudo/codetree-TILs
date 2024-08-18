n = int(input())
ans = []

def choose(cnt):
    if len(ans) == n:
        print(*ans)
        return
    
    for i in range(n, 0, -1):
        if not i in ans:
            ans.append(i)
            choose(cnt+1)
            ans.pop()
        else:
            continue
    return

choose(0)