

t = int(input())

for i in range(t):
    n = int(input())
    n_half = n/2
    n_mod = (n % 2) / 2
    result = int(n_half + n_mod)
    
    print(result)