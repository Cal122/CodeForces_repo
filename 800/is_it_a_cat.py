t = int(input())

meow_word_set = {"M","E","O","W"}

for i in range(0, t):
    str_len = int(input())
    meow_str = str(input()).upper()
    meow_str_set = set(meow_str)
    answer = "YES"
    
    if meow_word_set != meow_str_set or len(meow_str_set) != 4:
        print("NO")
        continue
    
    for s in range(len(meow_str)-1):
        if meow_str[s] == "M" and (meow_str[s+1] == "M" or meow_str[s+1] == "E"):
            pass
        elif meow_str[s] == "E" and (meow_str[s+1] == "E" or meow_str[s+1] == "O"):
            pass
        elif meow_str[s] == "O" and (meow_str[s+1] == "O" or meow_str[s+1] == "W"):
            pass
        elif meow_str[s] == "W" and (meow_str[s+1] == "W" or meow_str[s+1] == ""):
            pass
        else:
            answer = "NO"
    
    print(answer)