n, m, k = map(int, input().split())
move = list(map(int, input().split()))
grid = [i for i in range(1, m+1)]
pos = [0 for j in range(k)]
ans = 0
sco = []

def choose(cnt):
    global ans
    global sco
    if cnt == len(move)-1:
        ans = max(ans, len(sco))
        return
    
    for j in range(k):
        pos[j] += move[cnt]
        if grid[pos[j]%m] == 0:
            choose(cnt+1)
            pos[j] -= move[cnt]
            continue
        else:
            grid[pos[j]%m] = 0
            sco.append(1)
        choose(cnt+1)
        pos[j] -= move[cnt]
        sco.pop()
    return

choose(0)
            
print(ans)