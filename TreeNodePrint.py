from TreeNode import *

def toString(root, indent=0): # O(n) runtime
    if root == None:
        return ""
    return toString(root.right, indent+4)\
        + indent*" " + str(root.data)+"\n"\
        + toString(root.left, indent+4)

root1 = TreeNode(50)
root1.left = TreeNode(42)
root1.right = TreeNode(55)
root1.right.right= TreeNode(65)
root1.left.right = TreeNode(46)
root1.right.left = TreeNode(52)
root1.left.left = TreeNode(20)
print(toString(root1))
