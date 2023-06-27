melody = list(map(int, input().split()))

if melody[0] == 1:
    for i in range(7):
        if melody[i] != melody[i+1] - 1:
            print("mixed")
            exit()
        i += 1
    print("ascending")
    
elif melody[0] == 8:
    for i in range(7):
        if melody[i] != melody[i+1] + 1:
            print("mixed")
            exit()
        i += 1
    print("descending")

else:
    print("mixed")
