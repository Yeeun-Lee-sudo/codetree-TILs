n = int(input())
ans = 0
def sum(cnt):
    global ans
    ans += cnt
    if cnt == n:
        return ans
    else:
        cnt += 1
        sum(cnt)

sum(0)
print(ans)