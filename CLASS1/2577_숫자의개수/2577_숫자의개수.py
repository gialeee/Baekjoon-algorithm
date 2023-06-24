num = 1
count = [0 * n for n in range(10)]

for _ in range(3):
    num *= int(input())

for n in str(num):
    count[int(n)] += 1

for n in range(10):
    print(count[n])