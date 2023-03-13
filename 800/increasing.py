

t = int(input())

for i in range(t):
    n = int(input())
    integers = list(map(int, input().split()))
    ints_sorted = sorted(integers)
    answer = "YES"
    
    for i in range(0, len(ints_sorted) - 1):
        if ints_sorted[i] < ints_sorted[i+1]:
            continue
        else:
            answer = "NO"
    
    print(answer)