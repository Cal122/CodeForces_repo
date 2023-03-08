#EQUATION - (x**y * y) + (y**x * x) =n
#PROBLEM - Check if (x,y), a pair of integers <= n go into the formula (x**y * y) + (y**x * x) to equal n. If so, print (x,y), else print -1.
#SOLUTION - Loop at most n times to see if any pair of integers <= n go into the formula to equal n. If so, return (x,y)
#SOLUTION - 


def func(n):
    for i in range(0, n):
        for j in range(0,n):
            if i**j * j + j**i * i == n:
                return i,j
    return -1





test_cases = int(input())

print()
print()

for t in range(0, test_cases):
    n = int(input())
    print(func(n))


