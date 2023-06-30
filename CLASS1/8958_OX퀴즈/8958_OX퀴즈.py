cases = int(input())

for _ in range(cases):
    test = input()
    answer = 0
    streak = 0
    for result in test:
        if result == "O":
            streak += 1
        else:
            streak = 0
            
        answer += streak
    print(answer)
