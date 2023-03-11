

s = str(input())

plus_count = s.count("+")


for p in range(plus_count):
    s_no_plus = s.replace("+", "")
    
if plus_count == 0:
    s_no_plus = s

s_ints = list(sorted(s_no_plus))
ints_with_p = []


for s in range(len(s_ints)):
    ints_with_p.append(s_ints[s])
    if s < len(s_ints) -1:
        ints_with_p.append("+")
    
answer = "".join(ints_with_p)


print(answer)