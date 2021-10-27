def uppercount(s):
    '''
    Counts uppercase letters in an input string and returns number of them

    Keyword Arguments:
    S -- The input string that will have uppercases counted

    '''
    if len(s) == 0: #base case for if the string had no uppercases 
        return 0
    if len(s) == 1 and s[0] == '1': #base case for if the string has one uppercase
        return 1
    if (s[0]) == '1' and (s[-1]) == '1': #Base case (ending and beginning char are both 1, meaning all letters evaluated)
        return len(s)
    
    
    if ord(s[-1]) not in range(65,91): #if we're not looking at a caps letter
        s = s[:-1] #slice it out without adding a 1 to mark that an uppercase was found
    else: #if the letter evaluated is in fact uppercase
        s = str(1) + s[:-1] #add a 1 to beginning of letters and slice out the uppercase 
    return uppercount(s) #recursive part (keep feeding the remaining string back to function)

def clean_string(s):
    '''
    Returns new 'clean' string without anything that isn't a letter or space

    Keyword Arguments:
    s -- The string to be stripped down until only letters and spaces remain

    '''
    if len(s) == 0: #Base case: if everything is removed or evaluated 
        return '' 
    if (ord(s[0]) != 32) and (ord(s[0]) not in range(65,91)) and (ord(s[0]) not in range(97,123)): #if not char or space
        return clean_string(s[1:])    # remove from string and continue to recursive statement for further evaluation
    else:   #if previous [0] is valid and none removed
        return s[0] + clean_string(s[1:])  #recursive case: leave [0] alone and evaluate rest

def clean_list(l1,l2):
    '''
    Returns new list of elements that are in l1 but not in l2.
    
    Keyword Arguments:
    l1 -- list one: the list whose unique elements will be returned
    l2 -- list two: the list used for comparison to find out which elements in l1 are unique

    '''
    if l1 == []: #Base case: if everything has been evaluated or removed
        return []
    if l1[0] in l2: #if element being evaluated exists in l2
        return clean_list(l1[1:],l2) #recursively call function on rest of the string, slicing repeat element out
    else: #if element is unique 
        return [l1[0]] + clean_list(l1[1:],l2) #return [0] + rest of list after cleaning


