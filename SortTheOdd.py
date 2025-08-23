def sort_array(sa):
    odd_numbers = []
    
    for num in sa:
        if num % 2 != 0:
            odd_numbers.append(num)
    
    odd_numbers.sort()
    
    result = []
    odd_index = 0
    
    for num in sa:
        if num % 2 != 0:
            result.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            result.append(num)
    
    return result
