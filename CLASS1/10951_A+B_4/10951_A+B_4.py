import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    print(sum(map(int, line.split())))
