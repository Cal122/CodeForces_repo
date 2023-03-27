from itertools import permutations

t = int(input())

for i in range(t):
    n = int(input())
    unused_ints = set(map(int, input().split()))
    one_to_ten = {int(i) for i in range(0,10)}
    allowed_ints = list(one_to_ten - unused_ints)
    allowed_ints = [int(i) for i in allowed_ints for j in range(2)]
    perm_list = list(permutations(allowed_ints, 4))
    a = [list(i) for i in perm_list]
    counter = 0
    
    for i in range(len(a)):
        if len(set(a[i])) == 2:
            counter += 1

print(counter)