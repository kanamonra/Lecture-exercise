# Circular Linked list
# Blackpink circular linked list v01.03
# added del node def

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



def delete_node(delete_data):
    global head, current, pre

    if head.data == delete_data:		# 첫 번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current:		# 마지막 노드를 찾으면 반복 종료
            last = last.link		# last를 다음 노드로 변경
        last.link = head			# 마지막 노드의 링크에 head가 가리키는 노드 지정
        del current
        return

    current = head	                        	# 첫 번째 외 노드 삭제
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:  	# 중간 노드를 찾았을 때
            pre.link = current.link
            del current
            return


# section for array

head, current, pre = None, None, None
dataArray = ["Jennie", "Jisoo", "Lisa", "Rose", "Blackpink", 'Miyeon']

# Main section
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]  # first node

    head = node
# difference 4
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
    delete_node('Miyeon')
    printNodes(head)