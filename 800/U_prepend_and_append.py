

t = int(input())

for i in range(0, t):
    n = int(input())
    s = list(map(int, input()))
    result = 0
    
    if n == 0:
        print(0)
    
    elif (s[0] == 1 and s[-1] == 0) or (s[-1] == 1 and s[0] == 0):
        result = n-2
    
    else:
        result = n
    
    if result < 0:
        result = 0
    print(result)