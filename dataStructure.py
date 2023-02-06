# Circular Linked list
# Blackpink circular linked list v01.01

class Node:
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):   # printing node
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')

# difference 1
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData, insertData) :
    global head, current, pre

# difference 2
    if head.data == findData:		   # adding new head node
        node = Node()
        node.data = insertData
        node.link = head
        last = head		               # last node => head node
        while last.link != head:	   # last node => head then exit
            last = last.link	       # last => next node
        last.link = node		       # last link => new node link
        head = node
        return

    current = head
    while current.link != head:		# adding new middle node
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()			 # adding last node
    node.data = insertData
    current.link = node
    node.link = head

# section for array

head, current, pre = None, None, None
dataArray = ["Jennie", "Jisoo", "Lisa", "Rose", "Blackpink"]

# Main section
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]  # first node
    head = node
    node.link = head


    for data in dataArray[1:]:  # second node
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head


    printNodes(head)
