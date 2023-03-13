

t = int(input())

for i in range(0, t):
    full_list = []  
    
    empty = input()
    
    for i in range(8):
        full_list.append(str(input()))
    
    empty2 = input()
    
    red_rows = full_list.count("RRRRRRRR")
    
    print(red_rows)