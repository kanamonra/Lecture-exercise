# Singly linked list exercise

# make a class Node
class Node:
    def __init__(self):
        self.data = None
        self.link = None


# making first obj
node1 = Node()
# add data in node1 data type
node1.data = '사나'
print(node1.data, end=' ')

node2 = Node()
node2.data = '쯔위'
node1.link = node2
print(node2.data, end=' ')

# printing node1 linked data's detail
print(node1.link.data, end=' ')

current = node1
while current.link is not None:
    current = current.link
    print(current.data, end=' ')

# add new link data
newnode = Node()
newnode.data = "I'm new"
# connacting with link
newnode.link = node2.link
node2.link = newnode
# result checking
print(newnode.data)

node1.link = newnode.link
del(node2)

