def is_sortd_increasing(L):
    '''Evaluates whether or not the given list is sorted in increasing order, and returns true or false boolean value

    Keyword arguments:
    L -- The list object being evaluated
    
    '''
    index = 1 #loop is comparing current index to previous, so we want to start at one 
    while index < len(L): #iterating through the list, till end is reached
        if int(L[index]) < int(L[index-1]): #increasing means either equal or higher than last val, so I use '>' because it implies neither.
            return False
        index += 1
    return True   #no else statement needed, this case is only reached if False never returns
    
inpt = input('Please enter a list of numbers in the format 1,2,3,4 :')
inpt = inpt.split(',')
print(is_sortd_increasing(inpt))
