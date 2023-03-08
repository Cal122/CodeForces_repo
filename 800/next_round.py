#n = amount of contestants, k = given placement
#QUESTION - For a given index in a list of integers, find the amount of other integers in the list that are greater than or equal to the given index, return how many others there are.

inp1 = input().split(" ")
inp1_int = [int(i) for i in inp1]

n = inp1_int[0]
k = inp1_int[1]

inp2 = input().split(" ")
inp2_int = [int(s) for s in inp2]


advancers = 0

for integer in inp2_int:

    given_index = inp2_int[k-1]

    if integer <= 0:
        continue

    elif integer >= given_index and integer > 0:
        advancers += 1


print(advancers)