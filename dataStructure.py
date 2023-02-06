# Singly linked list exercise 02.01
# adding insert data def

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
    while current.link != None:       # looping
        current = current.link        # change the link to next
        print(current.data, end=" ")  # ending it
    print()  # printing it

def insert_nodes(find_data, insert_data):
    global memory, head, current, pre

    if head.data == find_data:  # head node add
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link != None:  # mid node add
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)  # last node add
    current.link = node

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
    insert_nodes('Pikachu', 'Cecegi')    # adding in first position
    printNodes(head)
    insert_nodes('Waterchu', 'Cecergi')   # adding in middle position
    printNodes(head)
    insert_nodes('Earthchu', 'Lifely')    # adding in last position
    printNodes(head)
