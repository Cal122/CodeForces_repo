n = int(input())

solution = 0

for i in range(n):
    integers = str(input())
    one_count = integers.count("1")
    if one_count >= 2:
        solution += 1

print(solution)