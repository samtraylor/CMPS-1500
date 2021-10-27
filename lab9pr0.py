from Node import *
from TreeNode import *

class LinkedList:
    
    def __init__(self, head=None): # O(1) runtime
        self.head = head
    def removeSpaces(self):
        s = ""
        current = self.head
        while current !=None:
            if current.data!=" ":
                s += str(current.data)
            current = current.next
        return s
    
head = Node("W")
head.next = Node(" ")
head.next.next = Node("a")
head.next.next.next = Node(" ")
head.next.next.next.next = Node("v")
head.next.next.next.next.next = Node(" ")
head.next.next.next.next.next.next = Node("e")
alist = LinkedList(head)
myString = alist.removeSpaces()
print(myString)

def tree_max(root):
    if root == None:
        return None
    if root.right ==  None:
        return root.data
    else:
        return tree_max(root.right)

root1 = TreeNode(50)
root1.left = TreeNode(42)
root1.right = TreeNode(55)
root1.right.right= TreeNode(65)
root1.left.right = TreeNode(46)
root1.right.left = TreeNode(52)
root1.left.left = TreeNode(20)
print(tree_max(root1))
