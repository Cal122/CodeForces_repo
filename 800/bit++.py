n = int(input())

operations = []
x = 0

for i in range(n):
    statement = list(map(str, input().split()))
    operations.extend(statement)
    
add_opps = (operations.count("++X") + operations.count("X++"))
sub_opps = (operations.count("--X") + operations.count("X--"))

for i in range(add_opps):
    x += 1

for i in range(sub_opps):
    x -= 1

print(x)
