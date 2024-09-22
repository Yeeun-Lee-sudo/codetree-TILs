n = int(input())

def f(num, cnt):
    if num == 1:
        #print(cnt)
        return cnt
    elif num % 2 == 0:
        num = num // 2
    else:
        num = num // 3
    cnt += 1
    #print(cnt, num)
    return f(num, cnt)

print(f(n, 0))