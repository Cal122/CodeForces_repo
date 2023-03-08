# Replace the middle of words that are longer than 10 characters with the number of characters between the first and last character.
# If len(word) <= 10 do nothing, if n == int do nothing,
 
n = int(input())

for i in range(0,n):
    word = str(input())
    word_length = len(word)
    numbers_between_word = str(word_length - 2)
    
    if word_length <= 10:
        print(word)
    

    

    else:
        new_word = word.replace(word[1:-1], numbers_between_word)
        print(new_word)

