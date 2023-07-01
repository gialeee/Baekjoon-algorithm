s = input()
alphabet = [-1 for _ in range(26)]

for idx, letter in enumerate(s):
    if alphabet[ord(letter) - ord('a')] == -1:
        alphabet[ord(letter) - ord('a')] = idx
    
for a in alphabet:
    print(a, end=" ")
