inp1 = input().split(" ")
inp1_int = [int(i) for i in inp1]

n = inp1_int[0]
k = inp1_int[1]
 
 
input = input()
str_input_list = input.split(" ")
int_input_list = [int(s) for s in str_input_list]
 
 
advancers = 0
 
for integer in int_input_list:
 
    given_index = int_input_list[k-1]
 
    if integer <= 0:
        continue
 
    elif integer >= given_index and integer > 0:
        advancers += 1
 
 
print(advancers)