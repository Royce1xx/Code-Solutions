def mxdiflg(a1, a2):
    
    great = 0
    if a2 == [] or a1 == []:
        return -1
    
    for i in range(len(a1)):
        for j in range(len(a2)):
            t =  abs(len(a1[i]) - len(a2[j]))
            if t >= great:
                great = t
    return great