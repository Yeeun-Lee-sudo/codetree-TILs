n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

arr = []
bomblist = []
def bomb1(x, y):
    arr.append([x, y])
    arr.append([x, y-1])
    arr.append([x, y-2])
    arr.append([x, y+1])
    arr.append([x, y+2])

def bomb2(x, y):
    arr.append([x, y])
    arr.append([x, y-1])
    arr.append([x-1, y])
    arr.append([x, y+1])
    arr.append([x+1, y])

def bomb3(x, y):
    arr.append([x, y])
    arr.append([x-1, y-1])
    arr.append([x-1, y+1])
    arr.append([x+1, y+1])
    arr.append([x+1, y-1])

def count(arr):
    res = []
    for i in arr:
        if i[0] < 0 or i[0] >= n:
            continue
        if i[1] < 0 or i[1] >= n:
            continue
        if i not in res:
            res.append(i)
    #print(*res)
    #print(len(res))
    return len(res)

max = 0

def search(bombs):
    #폭탄 놓을 위치를 저장해 둔 배열을 받음
    global max

    if len(bombs) == 0:
        a = count(arr)
        if a >= max:
            max = a
            #print(max)
        return

    for i in bombs:
        bomb1(i[0], i[1])
        search(bombs[1:])
        for j in range(5):
            arr.pop()

        bomb2(i[0], i[1])
        search(bombs[1:])
        for j in range(5):
            arr.pop()

        bomb3(i[0], i[1])
        search(bombs[1:])
        for j in range(5):
            arr.pop()
    return

for i in range(n):
    for j in range(n):
        if grid[j][i] == 1:
            bomblist.append([j, i])

#print(bomblist)
search(bomblist)
print(max)