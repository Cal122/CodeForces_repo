

i_mins = int(input())

min_times = list(map(int, input().split()))

first_val = min_times[0]
last_val = min_times[-1]

def function(x):
    
    for i in range(len(x) - 1):
        if (x[i+1] - x[i]) > 15:
            return x[i] + 15
    
    if 90 - last_val > 15:
        return last_val + 15
        

    
    return 90


if i_mins <= 1 and first_val <= 15:
    print(first_val + 15)

elif first_val > 15:
    print(15)

else:
    print(function(min_times))
