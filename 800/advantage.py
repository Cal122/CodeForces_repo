

t = int(input())


for i in range(t):
    n = int(input())
    partis = list(map(int, str(input()).split()))
    
    val_list = []
    sorted_partis = sorted(partis)
    
    for i in partis:
        max_num = sorted_partis[-1]
        if max_num == i:
            max_num = sorted_partis[-2]
        val_list.append(i - max_num)
        
        
    val_list = " ".join(str(i) for i in val_list)
    print(val_list)

