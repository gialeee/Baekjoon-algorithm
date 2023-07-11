N = int(input())
scores = list(map(int, input().split()))
new = 0

for score in scores:
    new += score/max(scores) * 100

print(new/N)
