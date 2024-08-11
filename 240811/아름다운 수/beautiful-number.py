n = int(input())

def p_arr(array):
    for i in array:
        print(i, end="")

arr = []
num = 0

def choose(len):
    global num
    if len == n:
        #p_arr(arr)
        #print()
        num += 1
        return

    for i in range(1, 5):
        for j in range(i):
            arr.append(i)
            #print(*arr)
            len = len + 1
        if len > n:
            for j in range(i):
                arr.pop()
                len = len - 1
            return
        choose(len)
        for j in range(i):
            arr.pop()
            len = len - 1
    return

choose(0)
print(num)