while True:
    line = input()

    if line == "0 0":
        break
    else:
        print(sum(map(int, line.split())))
