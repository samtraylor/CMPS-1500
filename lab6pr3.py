import random
import time


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

def analyze_mergesort(inputfile, outputfile):
    '''
    Takes name of input file, reads out integers line by line, sorts them
    using merge sort, and writes sorted ints out to specified file. Also, displays
    time taken to input values, to sort them, and to output them

    Keyword Arguments:
    inputfile -- the name of the file, ending in .txt , that stores the
                 unsorted ints
    outputfile -- the name of the file ending in .txt , where user would
                  like to store the sorted ints

    '''
    t = time.time()
    list2 = []
    openedfile = open(inputfile, 'r')
    ints = openedfile.readlines()
    for i in ints: #convert string elements to ints
        i = int(i)
        list2.append(i)
    t1 = time.time()
    print('It took ' + str(round(t1-t,6)) + ' seconds to input ' + str(len(ints)) + ' values from file ' + inputfile)
    openedfile.close()

    t2 = time.time()
    sortedlist = merge_sort(list2) #sort list
    t3 = time.time()
    print('It took ' + str(round(t3-t2,6)) + ' seconds to sort ' + str(len(ints)) + ' values using merge sort')

    t4 = time.time()
    output = open(outputfile, 'w')
    for x in range(len(sortedlist)):
        output.write(str(sortedlist[x]))
        output.write('\n')
    output.close()
    t5 = time.time()
    print('It took ' + str(round(t5-t4,6)) + ' seconds to output ' + str(len(ints)) + ' sorted values to file ' + outputfile)
    print('Total time the program took is ' + str(round(t1-t,6) + round(t3-t2,6) + round(t5-t4,6)) + ' seconds')

def analyze_selectionsort(inputfile, outputfile):
    '''
    Takes name of input file, reads out integers line by line, sorts them
    using selection sort, and writes sorted ints out to specified file.
    Also, takes time spend reading, sorting, and outputting data

    Keyword Arguments:
    inputfile -- the name of the file, ending in .txt , that stores the
                 unsorted ints
    outputfile -- the name of the file ending in .txt , where user would
                  like to store the sorted ints

    '''
    t = time.time()
    list2 = []
    openedfile = open(inputfile, 'r')
    ints = openedfile.readlines()
    for i in ints: #convert string elements to ints
        i = int(i)
        list2.append(i)
    t1 = time.time()
    print('It took ' + str(round(t1-t,6)) + ' seconds to input ' + str(len(ints)) + ' values from file ' + inputfile)
    openedfile.close()

    t2 = time.time()
    sortedlist = selection_sort(list2) #sort list
    t3 = time.time()
    print('It took ' + str(round(t3-t2,6)) + ' seconds to sort ' + str(len(ints)) + ' values using selection sort')

    t4 = time.time()
    output = open(outputfile, 'w')
    for x in range(len(sortedlist)):
        output.write(str(sortedlist[x]))
        output.write('\n')
    output.close()
    t5 = time.time()
    print('It took ' + str(round(t5-t4,6)) + ' seconds to output ' + str(len(ints)) + ' sorted values to file ' + outputfile)
    print('Total time the program took is ' + str(round(t1-t,6) + round(t3-t2,6) + round(t5-t4,6)) + ' seconds')

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
#analyze_mergesort(inputname,outputname)
#analyze_selectionsort(inputname,outputname)
#generate_nums('testingexp6.txt',1000000)
    
