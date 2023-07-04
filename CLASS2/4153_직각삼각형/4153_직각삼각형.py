while True:
    num = input()
    if num == "0 0 0":
        break
    else:
        sides = list(map(int, num.split()))
        hypo = max(sides)
        sides.remove(max(sides))
        
        if hypo**2 == sides[0]**2 + sides[1]**2:
            print("right")
        else: 
            print("wrong")