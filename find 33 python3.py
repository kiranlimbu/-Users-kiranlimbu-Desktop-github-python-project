def has_33(*args):
    '''
    FIND 33:
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    '''
    
    idx = 0
    idx_len = len(args) - 1
    
    for item in args:
        if args[idx] == 3:
            if idx == 0:
                if args[idx+1] == 3:
                    #print(f'idx1 {idx}')  #idx value check
                    return True
                elif 3 in args[:idx+1:-1]:
                    #print(args[:idx+1:-1])  #idx value check
                    #print(f'idx2 {idx}')   #idx value check
                    pass
                else:
                    #print(f'idx3 {idx}')   #idx value check
                    return False
            elif idx == idx_len:
                if args[idx-1] == 3:
                    #print(f'idx4 {idx}')   #idx value check
                    return True
                else:
                    #print(f'idx5 {idx}')   #idx value check
                    return False
            elif 0 < idx < idx_len:
                if  args[idx+1] == 3 or args[idx-1] == 3:
                    #print(f'idx6 {idx}')   #idx value check
                    return True
                elif 3 in args[:idx+1:-1]:
                    #print(args[:idx+1:-1]) #idx value check
                    #print(f'idx7 {idx}')   #idx value check
                    pass
                else:
                    #print(f'idx8 {idx}')   #idx value check
                    return False
   
        idx += 1
    print('no such value')
        
        
print(has_33(3,0,7,2,7,9,3,3,9,2))