# Circular Linked list
# Blackpink circular linked list v01.02
# added insert node def

class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):  # printing node
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')

    # difference 1
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(find_data, insert_data):
    global head, current, pre

    # difference 2
    if head.data == find_data:  # adding new head node
        node = Node()
        node.data = insert_data
        node.link = head
        last = head  # last node => head node
        while last.link != head:  # last node => head then exit
            last = last.link  # last => next node
        last.link = node  # last link => new node link
        head = node
        return

    current = head
    while current.link != head:  # adding new middle node
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()  # adding last node
    node.data = insert_data
    current.link = node
    # difference 3
    node.link = head


# section for array

head, current, pre = None, None, None
dataArray = ["Jennie", "Jisoo", "Lisa", "Rose", "Blackpink"]

# Main section
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]  # first node

    head = node
    # differnece 4
    node.link = head

    for data in dataArray[1:]:
        # second node
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        # difference 5
        node.link = head

    printNodes(head)
