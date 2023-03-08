n = int(input())

solution = 0

for i in range(0,n):
    integers = str(input())
    p_choice = int(integers[0])
    v_choice = int(integers[1])
    t_choice = int(integers[2])
    
    if len(integers) != 3:
        continue

    elif (p_choice + v_choice + t_choice) >= 2:
        solution += 1

print(solution)