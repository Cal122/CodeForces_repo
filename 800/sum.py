

t = int(input())

for i  in range(t):
    a,b,c = list(map(int, input().split()))
    answer = ""
    if a == b+c:
        answer = "YES"
    elif b == a+c:
        answer = "YES"
    elif c == a+b:
        answer = "YES"
    else:
        answer = "NO"
    
    print(answer)