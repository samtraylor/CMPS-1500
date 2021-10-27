from Node import *

def toStringRec(head):
    '''
    Returns string representation of linked list with head node head

    Keyword Arguments:
    Head --  name of the head node object in the linked list

    '''
    if head.next != None:
        return head.data + '->' + toStringRec(head.next)
    else:
        return head.data + '->'

def findElement(head,i):
    '''
    returns the data element at the i-th position of the linked list with heaD node head.

    Keyword Arguments:
    Head --  name of the head node object in the linked list
    i -- index of desired data element from list

    '''
    if i == 1:
        try:
            if head.next == None:
                return None
        except AttributeError:
            return None
    if i == 0:
        return head.data
    elif i != 0:
        i -= 1
        return findElement(head.next,i)


headN = Node('!')
node1 = Node('a')
node2 = Node('b')
headN.next = node1
node1.next = node2
print(toStringRec(headN))
