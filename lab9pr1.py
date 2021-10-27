from Node import *

class Queue:
    '''
    A first-in first-out queue (FIFO Queue) is a data structure that stores
    a linear list of items. It builds upon the link list functionality
    from the Node class.

    Attributes:
    head -- the item at front of queue
    rear -- last item in queue
    size -- number of items in queue

    '''
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def __repr__(self):
        current = self.head
        reprstr = ''
        s = self.size
        if s == 0:
            return 'head-> <-tail'
        elif s == 1:
            return 'head-> ' + str(self.head.data) + ' <-tail'
        else:
            while s >= 1:
                reprstr += str(current.data) +  ' '
                current = current.next
                s -= 1 
   
        return 'head-> ' + reprstr + '<-tail'
        
        
    def enqueue(self,item):
        '''
        Appends the new item at the end of the FIFO queue

        Keyword Args:
        item -- the node to be added

        '''
        s = self.size
        current = self.head
        if s == 0:
            self.head = Node(item)
            self.size = 1
            self.rear = self.head
        elif s > 1:
                while s > 1:
                    current = current.next
                    s -= 1 
                current.next = Node(item)
                self.rear = current.next
                self.size += 1
        else:
            self.head.next = Node(item)
            #print(self.front.data + self.rear.data)
            self.rear = self.head.next
            #print(self.front.data + self.rear.data)
            self.size = 2
            

    def dequeue(self):
        '''
        removes the front item from the queue and returns it. It returns
        None if the queue is empty.

        '''
        temp = []
        if self.size == 0:
            return None
        else:
            temp.append(self.head.data)
            self.head.data = None
            self.head = self.head.next 
            self.size -= 1
            return temp[0]

    def isEmpty(self):
        '''
        returns True if the queue is empty, and False otherwise.

        '''
        state = False
        if self.size == 0:
            state = True
        else:
            state = False
        return state
        
