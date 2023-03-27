

t = int(input())

for i in range(t):
    
    answer = "NO"
    
    fb_string = "FBFFBFFBFBFFBFFB" * 100
    
    s_len = int(input())
    s = str(input())
    
    if s in fb_string:
        answer = "YES"
    
    print(answer)
    