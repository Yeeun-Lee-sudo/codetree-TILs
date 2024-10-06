a, b, c, d = map(int, input().split())

if d < b:
    c = c - 1
    d = d + 60

print((c-a)*60 + (d-b))