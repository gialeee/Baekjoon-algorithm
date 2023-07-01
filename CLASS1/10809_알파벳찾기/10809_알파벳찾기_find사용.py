string = str(input())

for i in range(26) :
    print(string.find(chr(97+i)), end = ' ')  # find() 리턴값 없으면 -1 반환
