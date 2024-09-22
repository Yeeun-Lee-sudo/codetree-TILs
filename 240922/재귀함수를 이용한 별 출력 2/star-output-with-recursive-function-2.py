n = int(input())

def star(num, cnt):
    if cnt > 2 * n:
        return
    
    print("* " * num)
    cnt += 1
    if cnt > n + 1 :
        num += 1
    elif cnt == n + 1:
        num = num
    else:
        num -= 1
    
    star(num, cnt)

star(5, 1)