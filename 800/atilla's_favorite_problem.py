import string

letters = list(string.ascii_lowercase)

t = int(input())

for i in range(0, t):
    n = int(input())
    s = str(input())
    nums = []
    
    for l in s:
        nums.append(letters.index(l)+1)
    
    answer = max(nums)
    print(answer)


