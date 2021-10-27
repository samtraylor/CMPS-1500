from Node import *

def removeSpaces(s):
    newS = ''
    for c in s:
        if c !=" ":
            newS += c
    return newS

myString = "Hello world"
myString = removeSpaces(myString)
print(myString) #Should print "Helloworld"

def removeSpaces2(L):
    newL = []
    for c in L:
        if c!=" ":
            newL += [c]
    L = newL
    return L
        
myList = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
myString = removeSpaces2(myList)
print(myString) #Should print [’H’, ’e’, ’l’, ’l’, ’o’, ’w’, ’o’, ’r’, ’l’, ’d’]

class Person:
    def __init__(self,F,N):
        self.firstName = F
        self.lastName = N
    def __repr__(self):
        return self.firstName + ' ' + self.lastName

def toString(head):
    '''
    Returns string representation of linked list  with node head

    Keyword Arguments:
    head -- node that you want to be head of linked list

    '''
    string = ''
    current = head
    while current != None:
        string += (str(current.data) + '->')
        current = current.next
    return string
    

'''headN = Node('!')
node1 = Node('a')
node2 = Node('b')
headN.next = node1
node1.next = node2
print(toString(headN))'''
    
    
