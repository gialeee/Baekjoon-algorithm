tests = int(input())

for _ in range(tests):
    h, w, n = map(int, input().split())
    x = h if n % h == 0 else n % h
    y = n // h if n % h == 0 else (n // h) + 1

    print(f'{x}{y:02d}')