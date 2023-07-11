L = int(input())
string = input()
answer = 0

for i, letter in enumerate(string):
    answer += ((ord(letter) - ord('a') + 1) * (31**i))

print(answer % 1234567891)