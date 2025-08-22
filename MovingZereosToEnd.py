def move_zeros(lst):
    
    royce = []
    
    t = lst.count(0)
    for i in range(len(lst)):
        
        if lst[i] != 0:
            royce.append(lst[i])
            
            
    for i in range(t):
        royce.append(0)
        
    return royce