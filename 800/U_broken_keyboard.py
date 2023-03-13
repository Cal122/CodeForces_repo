# (word length // 3) gives the amount of pairs of integers needed to be checked



t = int(input())

for i in range(0, t):
    
    word_length = int(input())
    word = list(str(input()))
    comparison_num = word_length // 3
    substrings = []
    counter = 0
    
    for i in range(comparison_num):
        substrings.append(word[i*comparison_num: i*comparison_num + 3])
    
    for list in substrings:
        print(list)



if word_length <= 2:
    answer = "NO"

print(comparison_num)
print(substrings)