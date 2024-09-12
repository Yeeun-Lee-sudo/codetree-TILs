n , m = map(int, input().split())
list_A = list(map(int, input().split()))

def f(m):
    ans = list_A[0]
    while(m != 1):
        ans += list_A[m-1]
        if m%2 == 1:
            m -= 1
        else:
            m = m // 2
    return ans

print(f(m))