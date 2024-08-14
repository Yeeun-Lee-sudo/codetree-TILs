n, m, k = map(int, input().split())
move = list(map(int, input().split()))
grid = [1 for i in range(m)]
pos = [1 for j in range(k)]
ans = 0
sco = []

def choose(cnt):
    global ans
    global sco
    if cnt == len(move):
        #print(*pos)
        ans = max(ans, sum(sco))
        return
    
    for j in range(k):
        if pos[j] >= m:
            choose(cnt+1)
            continue
        
        pos[j] += move[cnt]
        if pos[j] >= m:
            sco.append(1)
            #print(*pos)
        else:
            sco.append(0)
        choose(cnt+1)
        pos[j] -= move[cnt]
        sco.pop()
    return

choose(0)
            
print(ans)