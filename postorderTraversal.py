class _BinTreeNode :
    def __init__( self, data ):
        self.data = data
        self.left = None
        self.right = None

def postorderTrav( subtree ):
        if subtree is not None :
            postorderTrav( subtree.left )
            postorderTrav( subtree.right )
            print( subtree.data )
            

node1 = _BinTreeNode('A')
node2 = _BinTreeNode('B')
node3 = _BinTreeNode('C')
node4 = _BinTreeNode('D')
node5 = _BinTreeNode('E')
node6 = _BinTreeNode('F')
node7 = _BinTreeNode('G')
node8 = _BinTreeNode('H')
node9 = _BinTreeNode('I')
node10 = _BinTreeNode('J')


node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node8

node3.left = node6
node3.right = node7
node7.left = node9
node7.right = node10

postorderTrav(node1)

