height = int(input())

for i in range(height):
    stars = "*" * (i + 1)
    print(f"{stars : >{height}}")