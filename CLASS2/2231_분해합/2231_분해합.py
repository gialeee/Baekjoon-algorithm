N = int(input())

for i in range(N):
    M = i
    for j in range(len(str(i))):
        M += int(str(i)[j])
    
    if M == N:
        print(i)
        quit()
        
print(0)