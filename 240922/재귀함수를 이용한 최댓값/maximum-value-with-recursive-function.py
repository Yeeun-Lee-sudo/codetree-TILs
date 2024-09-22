n = int(input())
nums = list(map(int, input().split()))

def max(m, n):
    if n == 0:
        return m 
    if m > nums[n]:
        return max(m, n-1)
    else:
        return max(nums[n], n-1)

print(max(0, n-1))