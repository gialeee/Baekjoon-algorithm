N = int(input())

depth = 1
hive_num = 1

while N > hive_num:
    hive_num += 6 * depth
    depth += 1

print(depth)