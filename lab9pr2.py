from TreeNode import *

def getheight(root):
    '''
    takes as input a root node of a binary (search) tree, and returns its height.

    '''
    if root == None: #if nonexistant
        return 0
    elif root.right != None and root.left != None: #if node exists with both children
        #print('right is' + str(root.right.data) + 'left is' + str(root.left.data))
        return max(getheight(root.left),getheight(root.right)) + 0
    else:
        return max(getheight(root.left),getheight(root.right)) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

print(getheight())
