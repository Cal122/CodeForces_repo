

t = int(input())

for i in range(0, t):
    
    n = int(input())
    times = list(map(int, input().split()))
    walk_amount = 0
    last_number = times[-1]
    mins_in_day = 1440
    
    for n in range(len(times) - 1): 
        
        if times[n+1] - times[n] >= 360:
            walk_amount += 3
        
        elif times[n+1] - times[n] >= 240:
            walk_amount += 2
        
        elif times[n+1] - times[n] >= 120:
            walk_amount += 1

    if walk_amount >= 2 or mins_in_day - last_number >= 120:
        print("YES")
    
    elif walk_amount <2:
        print("NO")