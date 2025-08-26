def delete_nth(order, max_e):
    tommy = []
    royce = {}
    
    for key in order:
        if key not in royce:
            royce[key] = 0

        if royce[key] < max_e:
            tommy.append(key)
            royce[key] += 1

    return tommy