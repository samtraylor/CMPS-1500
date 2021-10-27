import random

def merge_sort(aList):
    """
    Merge sort recursively divides the list into half, sorts both halves
    and then merges the two sorted lists into one.
    """
    # If the aList is size 0 or 1, it's already sorted.
    if len(aList) <= 1:
        return aList

    else:
        mid = len(aList) // 2

        # Recursively sort each half
        left = merge_sort(aList[:mid]) # left half, L[0..n/2-1]
        right = merge_sort(aList[mid:]) # right half, L[n/2..n-1]
        
        # Merge the two (each sorted) parts back together
        return merge(left, right)

                                
def merge(left, right):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0

    # Repeatedly move the smallest of left and right to the new list
    while lt < len(left) and rt < len(right):
        if left[lt] < right[rt]:
            aList.append(left[lt])
            lt += 1
        else:
            aList.append(right[rt])
            rt += 1

    # There will only be elements left in one of the original two lists.

    # Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append(left[lt])
        lt += 1
         
    # Append the remains of right (rt..end) on to the new list.
    while rt < len(right):
        aList.append(right[rt])
        rt += 1

    return aList

def selection_sort(aList):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len(aList)
  for i in range(n-1):
    
      
    # Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    # Determine if any other element contains a smaller value.
    for j in range(i+1, n):
      if aList[j] < aList[smallNdx]:
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[i]
    aList[i] = aList[smallNdx]
    aList[smallNdx] = tmp

  return aList  

def use_mergesort(inputfile, outputfile):
    '''
    Takes name of input file, reads out integers line by line, sorts them
    using merge sort, and writes sorted ints out to specified file

    Keyword Arguments:
    inputfile -- the name of the file, ending in .txt , that stores the
                 unsorted ints
    outputfile -- the name of the file ending in .txt , where user would
                  like to store the sorted ints

    '''
    list2 = []
    openedfile = open(inputfile, 'r')
    ints = openedfile.readlines()
    for i in ints: #convert string elements to ints
        i = int(i)
        list2.append(i)
    openedfile.close()
    
    sortedlist = merge_sort(list2)
    
    output = open(outputfile, 'w')
    for x in range(len(sortedlist)):
        output.write(str(sortedlist[x]))
        output.write('\n')
    output.close()

def use_selectionsort(inputfile, outputfile):
    '''
    Takes name of input file, reads out integers line by line, sorts them
    using selection sort, and writes sorted ints out to specified file

    Keyword Arguments:
    inputfile -- the name of the file, ending in .txt , that stores the
                 unsorted ints
    outputfile -- the name of the file ending in .txt , where user would
                  like to store the sorted ints

    '''
    list2 = []
    openedfile = open(inputfile, 'r')
    ints = openedfile.readlines()
    for i in ints: #convert string elements to ints
        i = int(i)
        list2.append(i)
    openedfile.close()
    
    sortedlist = selection_sort(list2)
    
    output = open(outputfile, 'w')
    
    for x in range(len(sortedlist)):
        output.write(str(sortedlist[x]))
        output.write('\n')

    output.close()

def generate_nums(filename,n):
    random.seed(0)
    createdfile = open(filename, 'w')
    for x in range(n):
        if x != 0:
            createdfile.write('\n')
        createdfile.write(str(random.randrange(100)))
    createdfile.close()

#inputname = input()
#outputname = input()
#use_mergesort(inputname,outputname)
#use_selectionsort(inputname,outputname)
#generate_nums('testing.txt',5)
    
