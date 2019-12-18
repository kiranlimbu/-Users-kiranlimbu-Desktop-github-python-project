def blackjack(a,b,c):
    '''
    BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
    '''
    num = [a,b,c]
    new_sum = 0
    
    if sum(num) == 21:
        return sum(num)
    elif sum(num) > 21:
        if 11 in num:
            new_sum = sum(num) - 10
            if new_sum > 21:
                return 'Bust'
            else:
                return new_sum
        else:
            return 'Bust'
    else:
        return sum(num)
        
    
print(blackjack(8,11,9))