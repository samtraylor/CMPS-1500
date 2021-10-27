def is_sorted(lst):
    '''Takes input as list of numbers, returns Boolean True if list is sorted in increasing order, returns  false otherwise

    Keyword Arguments:
    lst -- The list object being evaluated

    '''
    if len(lst) < 2:     #if final 2-digit comparison is completed, one element deletes leaving one left (we know we're done)
        return True     #all numbers have been compared without the program ending to return False
    elif int(lst[1]) < int(lst[0]):    #if element following the 0th element is not equal or greater
        return False    #stop and return false, we're already done
    else:   #if [1] is an increase or same as [0], we move our search one index forward
        return(is_sorted(lst[1:]))  #we move our search one index forward and recurse, now working with a smaller list

#print(is_sorted([1,2,3,4,5]))
#print(is_sorted([1,2,3,3,3,4,5]))
#print(is_sorted([1,2,3,2,5,5]))
#print(is_sorted([5,4,3,2,1]))
        
def is_file_sorted(filename):
    '''Takes as input the name of an input file (ending in .txt) containing list of int nums, one per line, returns Boolean True if list is sorted in increasing order, returns  false otherwise

    Keyword Arguments:
    filename -- The file containing intergers  to be used as list

    '''
    i = 1
    lstfile = open(filename, 'r')
    lines = lstfile.readlines() #reads as list
    lstfile.close()
    while i < len(lines):
        if int(lines[i]) < int(lines[i-1]): #if previous  number is greater than current
            return False #we know the list isn't always increasing, so return false
        i += 1
    return True #if loop completees without any return ending it, every element passed the tests
    
#print(is_file_sorted('testingfile1.txt'))
#print(is_file_sorted('testingfile2.txt'))
#print(is_file_sorted('testingfile3.txt'))

    
    
