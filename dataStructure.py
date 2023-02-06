# Singly linked list exercise 02.01
# adding delete data def

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
    while current.link != None:  # looping
        current = current.link  # change the link to next
        print(current.data, end=" ")  # ending it
    print()  # printing it


def insert_nodes(find_data, insert_data):
    global head, current, pre

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

    node = Node()  # last node add
    current.link = node


def del_data(delete_data):
    global head, current, pre

    if head.data == delete_data:         # deleting first postion data
        print(f'Successfully deleted first position data')
        current = head
        head = head.link
        del current
        return

    current = head
    while current.link != None:   # del middle or last position data

        pre = current
        current = current.link
        if current.data == delete_data:
            print(f'Successfully deleted middle position data')
            pre.link = current.link
            del current
            return
    # non positioning data will be exquisite program  // no difference
    print(f'Successfully deleted last position data')


def search_data(search_data):
    global head, current, pre

    current = head   # for search a head to middle pos
    if current.data == search_data:
        return current   # found it then return

    while current.link != None:  # not find then do this func
        current = current.link
        if current.data == search_data:
            return current  # if head is not, then search from current then return
    return Node()  # empty non returns


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
    # memory.append(node)    => not using at all
    # making pre

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        # pre.link = node  => this will cut the relation between others
        # result: only pikachu

        # memory.append(node)  => not using at all

    printNodes(head)
    insert_nodes('Pikachu', 'Cecegi')  # adding in first position
    printNodes(head)
    insert_nodes('Waterchu', 'Cecergi')  # adding in middle position
    printNodes(head)
    insert_nodes('Earthchu', 'Lifely')  # adding in last position
    printNodes(head)
    del_data('Cecegi')         # deleting in first position
    printNodes(head)
    del_data('Lifely')         # del mid
    del_data('Cecergi')        # del last
    printNodes(head)

    print(search_data('Lightchu').data)   # without data => return node memory
    print(search_data('Ceccegi').data)    # with data => return 'None'
