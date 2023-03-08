#PROBLEM - Compare each index with the index infront of it and check if it's the same, if so, add one to the counter, if not, move to next index and repeat
#PROBLEM_2 - If a string is repeated 7 times in a row, 
#SOLUTION -

players_string = list(str(input()))

int_counter = 1

for s in range(len(players_string)-1):
    
    if int_counter == 7:
        break
    
    elif players_string[s] == players_string[s+1]:
        int_counter += 1
    
    else:
        int_counter = 1


if int_counter >= 7:
    print("YES")
else:
    print("NO")