h, m = map(int, input().split())

if m >= 45:
    m -= 45
elif h == 0:
    h = 23
    m += 60 - 45
else:
    h -= 1
    m += 60 - 45

print(h, m)