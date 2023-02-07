# queue 큐
# First in first out


def is_queue_full():
    global SIZE, queue, front, rear
    if rear != SIZE - 1:
        return False
    elif rear == SIZE and front == -1:
        return True
    else:
        # loop 3 times for find front does have any empty space after delete
        for i in range(front + 1, SIZE):
            queue[i - 1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


def is_queue_empty():
    global SIZE, queue, front, rear
    if front == -1 and rear == -1:
        return True
    elif front == rear:
        return True
    else:
        return False


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print('Queue is empty!')
        return None
    return queue[front + 1]


def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print('Queue is full!')
        return
    rear += 1
    queue[rear] = data


def de_queque():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print('Queue is empty!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__":
    print('Please select')
    menu = input("Input data(I)/Eliminate(E)/View(V)/Exit program(X) ==> ")

    while menu != 'X' and menu != 'x':
        if menu == 'I' or menu == 'i':
            data = input("Input data ==> ")
            en_queue(data)
            print("Current Queue : ", queue)
        elif menu == 'E' or menu == 'e':
            data = de_queque()
            print("Delete data ==> ", data)
            print("Current Queue : ", queue)
        elif menu == 'V' or menu == 'v':
            data = peek()
            print("View data ==> ", data)
            print("Current Queue : ", queue)
        else:
            print("Wrong selection")

        menu = input("Input data(I)/Eliminate(E)/View(V)/Exit program(X) ==> ")

    print("Thank you")
