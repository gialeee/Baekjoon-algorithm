a, b = map(int, input().split())
multiple = a*b

while a%b != 0:
    a, b = b, a%b

print(b)
print(multiple//b)