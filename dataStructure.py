# binary tree
# self exercise -> binary tree -> for shin chan
# left woman goes, right man goes

class tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


node1 = tree_node()
node1.data = 'Shin chan relationship status'

node2 = tree_node()
node2.data = 'Family members'
node1.left = node2

node3 = tree_node()
node3.data = 'Friends'
node1.right = node3

node4 = tree_node()
node4.data = 'Female members'
node2.left = node4

node5 = tree_node()
node5.data = 'Male members'
node2.right = node5

node6 = tree_node()
node6.data = 'Female friends'
node3.left = node6

node7 = tree_node()
node7.data = 'Male friends'
node3.right = node7

node8 = tree_node()
node8.data = 'Nene chan'
node6.right = node8

node9 = tree_node()
node9.data = 'Toru kun'
node7.right = node9

node10 = tree_node()
node10.data = 'Misae (mom)'
node4.left = node10

node11 = tree_node()
node11.data = 'Nohara (dad)'
node5.right = node11

def preorder(node):
    if node is None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end="->")
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end="->")


print('Pre order : ', end='')
preorder(node1)
print('Done')

print('In order : ', end='')
inorder(node1)
print('Done')

print('Post order : ', end='')
postorder(node1)
print('Done')