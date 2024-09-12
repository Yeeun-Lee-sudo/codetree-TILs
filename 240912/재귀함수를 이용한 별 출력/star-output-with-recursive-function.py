n = int(input())

def star(cnt):
    if cnt == n + 1:
        return
    
    print("*"*cnt)
    star(cnt+1)

star(1)