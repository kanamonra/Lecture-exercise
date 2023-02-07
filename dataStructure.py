# circular queue 큐
# making circular queue ex 263p


def is_queue_full():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, queue, front, rear
# change
    if front == rear:
        return True
    else:
        return False


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print('Queue is empty!')
        return None
# change
    return queue[(front + 1) % SIZE]


def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print('Queue is full!')
        return
    # connecting with rear ~ front
# change
    rear = (rear+1) % SIZE
    queue[rear] = data


def de_queque():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print('Queue is empty!')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


SIZE = int(input('Enter queue size: '))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":
    print('Please select')
    menu = input("Input data(I)/Eliminate(E)/View(V)/Exit program(X) ==> ")

    while menu != 'X' and menu != 'x':
        if menu == 'I' or menu == 'i':
            data = input("Input data ==> ")
            en_queue(data)
            print("Current Queue : ", queue)
            print("front: ", front, ",rear", rear)
        elif menu == 'E' or menu == 'e':
            data = de_queque()
            print("Delete data ==> ", data)
            print("Current Queue : ", queue)
            print("front: ", front, ",rear", rear)
        elif menu == 'V' or menu == 'v':
            data = peek()
            print("View data ==> ", data)
            print("Current Queue : ", queue)
            print("front: ", front, ",rear", rear)
        else:
            print("Wrong selection")

        menu = input("Input data(I)/Eliminate(E)/View(V)/Exit program(X) ==> ")

    print("Thank you")
