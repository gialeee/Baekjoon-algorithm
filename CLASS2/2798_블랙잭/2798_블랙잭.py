N, M = map(int, input().split())
numbers = list(map(int, input().split()))
max = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = numbers[i] + numbers[j] + numbers[k]
            if max < sum <= M:
                max = sum

print(max)