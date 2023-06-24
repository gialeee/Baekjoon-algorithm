numbers = {}

for n in range(1, 10):
    numbers[int(input())] = n

print(max(numbers.keys()))
print(numbers[max(numbers.keys())])