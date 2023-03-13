#EQUATION - (x**y * y) + (y**x * x) =n
#PROBLEM - Check if (x,y), a pair of integers <= n go into the formula (x**y * y) + (y**x * x) to equal n. If so, print (x,y), else print -1.
#SOLUTION - Loop at most n times to see if any pair of integers <= n go into the formula to equal n. If so, return (x,y)


t = int(input())

for i in range(0, t):
    n = int(input())
    answer = None
    
    for j in range(0, n):
        for k in range(0, n):
            while answer == None:
                if (j ** k * k) + (k ** j * j) == n:
                    answer = j,k
                    break
                
        
    print(answer)