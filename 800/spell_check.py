from itertools import permutations

t = int(input())

for i in range(t):
    
    s_len = int(input())
    s = str(input())
    
    answer = "NO"
    
    permutation_list = list(permutations(list("Timur")))
    
    for perm in permutation_list:
        if perm == tuple(s):
            answer = "Yes"
            break
    
    print(answer)