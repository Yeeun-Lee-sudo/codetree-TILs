k, n = map(int, input().split())
ans = []
tf = 0
bf = 0

def choose(cnt): 
    global tf
    global bf

    if len(ans) == n:
        print(*ans)
        return
    
    for i in range(1, k+1):
        if bf == i:
            if tf == 1:
                continue
            ans.append(i)
            tf = 1
            choose(cnt+1)
            ans.pop()
        else:
            ans.append(i)
            bf = i
            choose(cnt+1)
            ans.pop()

choose(0)