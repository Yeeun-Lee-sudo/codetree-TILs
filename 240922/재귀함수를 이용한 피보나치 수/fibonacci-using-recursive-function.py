n = int(input())

def nums(n1, n2, cnt):
    if cnt == n - 1:
        return n1 + n2
    else:
        return nums(n2, n1+n2, cnt+1)

print(nums(1, 1, 2))