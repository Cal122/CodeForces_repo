

l1 = str(input())
l2 = str(input())

l3 = []


for i in range(len(l1)):
    if l1[i] == l2[i]:
        l3.append("0")
    else:
        l3.append("1")

l3_str = "".join(l3)

print(l3_str)