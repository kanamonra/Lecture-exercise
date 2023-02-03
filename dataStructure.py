# Singly linked list exercise

# make a class Node
class Node:
    def __init__(self):
        self.data = None
        self.link = None


# print nodes head, pre, current
def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=" ")
    print()


memory = []
head, pre, current = None, None, None
dataArray = ['Pikachu', 'Lightchu', 'Waterchu', 'Firechu', 'Earthchu']
# making head
# node1 = Node()
# node1.data = dataArray[0]
# head = node1
# memory.append(node1)

if __name__ == "__main__":
    # making head
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)
    # making pre
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        # pre.link = node  => this will cut the relation between others
        # result: only pikachu
        memory.append(node)

    printNodes(head)
