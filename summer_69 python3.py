def summer_69(*args):
    '''
    SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting 
    with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
    '''
    mylist = []
    num1 = 0
    num2 = 0
    idx = 0
    idx1 = 0
    
    for item in args:
        if 6 in args and 9 in args:
            if item == 6 in args:
                num1 = idx
            elif item == 9 in args:
                num2 = idx
        else:
            return 'missing 6 and/or 9'
        idx += 1
    
    for item in args:
        if idx1 < num1 or idx1 > num2:
            mylist.append(item)
        idx1 += 1    
    return sum(mylist)
            
        
print(summer_69(1,2,6,0,9,3))