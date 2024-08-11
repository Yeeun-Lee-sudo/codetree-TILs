n = int(input())
bombed_m = [ [False for i in range(n)] for j in range(n)]
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
bomblist = []

for i in range(n):
    ll = list(map(int, input().split()))
    if 1 in ll:
        bomblist.append([ll.index(1), i])

#print(bomblist)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def bomb(x, y, b_type):
    # 폭탄 종류마다 터질 위치를 미리 정의합니다.
    bomb_shapes = [
        [], 
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]

    # 격자 내 칸에 대해서만 영역을 표시합니다.
    for i in range(5):
        dx, dy = bomb_shapes[b_type][i];
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bombed_m[nx][ny] = True

    #print(arr)

ans = 0

def count():
    for i in range(n):
        for j in range(n):
            bombed_m[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])

    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed_m[i][j]:
                cnt += 1
    
    return cnt

def search(bombs):
    #폭탄 놓을 위치를 저장해 둔 배열을 받음
    global ans

    if len(bombs) == 0:
        ans = max(ans, count())
        return

    for i in bombs:
        for j in range(3):
            bomb_type[i[1]][i[0]] = j
            search(bombs[1:])

    return

search(bomblist)
print(ans)