k, n = map(int, input().split())
arr = []

def choose(index):
    if index >= n:
        print(*arr)
        return

    for i in range(1, k+1):
        arr.append(i)
        choose(index+1)
        arr.pop()
    return



choose(0)