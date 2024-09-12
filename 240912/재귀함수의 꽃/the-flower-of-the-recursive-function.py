n = int(input())
upper = 0

def f(num):
    global upper
    if num == 0:
        upper = 1
        return

    print(num, end=" ")
    if upper == 0:
        f(num-1)
    if upper == 1:
        print(num, end=" ")
        return

f(n)