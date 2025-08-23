def array_diff(a, b):
    remove = set(b)
    out = []
    for x in a:
        if x not in remove: 
            out.append(x)
    return out