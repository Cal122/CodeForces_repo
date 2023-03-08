# problems with ur and duur
# seems that it it doesn't return correct answer if (1,1) is only the final answer


t = int(input())

for i in range(0, t):
    x = 0
    y = 0
    n = int(input())
    s = str(input().lower())
    answer = ""
    for l in s:
        if x == 1 and y == 1:
            answer = "YES"
            break
        elif l == "l":
            x -= 1
        elif l == "r":
            x += 1
        elif l == "u":
            y += 1
        elif l == "d":
            y -= 1
    
    if x == 1 and y == 1:
        answer = "YES"
    elif x != 1 and y != 1:
        answer = "NO"
    else:
        answer = "NO"
    print(answer)