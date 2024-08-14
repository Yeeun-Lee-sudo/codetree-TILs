k, n = map(int, input().split())
ans = []

def choose(cnt): 
    global tf
    global bf

    if len(ans) == n:
        print(*ans)
        return
    
    for i in range(1, k+1):
        if len(ans) >= 2:
            if ans[-1] == ans[-2] == i:
                #print("aaa")
                continue
        ans.append(i)
        choose(cnt+1)
        ans.pop()
    return

choose(0)