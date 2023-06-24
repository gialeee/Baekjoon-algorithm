# input : T \n R S -> P
T = int(input())
P = ""

for _ in range(T):
    R, S = input().split()
    for letter in S:
        P += letter * int(R)
    P += "\n"

print(P)