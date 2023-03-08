t = int(input())

for i in range(0, t):
    integers = []
    a,b,c = map(int, str(input()).split())
    integers.extend([a,b,c])
    integers = sorted(integers)
    midpoint = len(integers) // 2
    result = integers[midpoint]
    print(result)