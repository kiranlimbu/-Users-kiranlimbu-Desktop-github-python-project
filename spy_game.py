def spy_game(*args):
    '''
    SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
    '''
    mylist = []
    idx = 0
    num1 = 0
    num2 = 0
    num3 = 0
    
    for item in args:
        if item == 0 or item == 7:
            mylist.append(item)
            if item == 7:
                break
    
    for item in mylist:
        if mylist[idx] == 0:
            if num1 == idx:
                num1 = idx
            else:
                num2 = idx
        elif mylist[idx] == 7:
            num3 = idx
        idx += 1
    
    if num1 < num2 < num3:
        return True
    else:
        return False

print(spy_game(0,2,9,0,7))