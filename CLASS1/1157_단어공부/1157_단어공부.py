word = input()
letters = {}

for letter in word:
    if letter.upper() not in letters:
        letters[letter.upper()] = 0
    letters[letter.upper()] += 1

max_keys = [key for key, value in letters.items() if value == max(letters.values())]
if len(max_keys) == 1:
    print(max(letters, key=letters.get))
else:
    print("?")
