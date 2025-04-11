def get_biggest(numbers):
    
    if numbers:
        
        dict_numbers = {}
        
        for n in numbers:
            num = str(n)
            if num[0] not in dict_numbers:
                dict_numbers[num[0]] = [num]
            else:
                dict_numbers[num[0]].append(num)
                
                
    
    else:
        return -1