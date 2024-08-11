n = int(input())
arr = []
bomblist = []

for i in range(n):
    ll = list(map(int, input().split()))
    if 1 in ll:
        bomblist.append([ll.index(1), i])

#print(bomblist)
'''

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

'''

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def bomb(x, y, b_type):
    # 폭탄 종류마다 터질 위치를 미리 정의합니다.
    bomb_shapes = [
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]
    num = 0
    # 격자 내 칸에 대해서만 영역을 표시합니다.
    for i in range(5):
        dx, dy = bomb_shapes[b_type][i];
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            arr.append([nx, ny])
            num += 1
    return num
    #print(arr)

def count(arr):
    res = []
    for i in arr:
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
        for j in range(3):
            nn = bomb(i[1], i[0], j)
            search(bombs[1:])
            for p in range(nn):
                arr.pop()

    return

search(bomblist)
print(max)