n = int(input())

def printh(n, cnt):
    if cnt == n:
        return
    
    print("HelloWorld")
    printh(n, cnt+1)

printh(n, 0)