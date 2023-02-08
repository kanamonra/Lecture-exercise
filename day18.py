# Chapter 4
# Graph for friends that has ...

class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]




# making g1 and give data
g1 = None
stack = []
visited_array = []
name_array = []

# main section
SIZE = 9
g1 = graph(SIZE)

g1.graph[0][1] = 1
g1.graph[0][2] = 1
g1.graph[0][4] = 1

g1.graph[1][0] = 1
g1.graph[1][2] = 1
g1.graph[1][3] = 1

g1.graph[2][0] = 1
g1.graph[2][1] = 1
g1.graph[2][4] = 1
g1.graph[2][5] = 1

g1.graph[3][1] = 1
g1.graph[3][2] = 1
g1.graph[4][0] = 1
g1.graph[4][2] = 1
g1.graph[4][6] = 1

g1.graph[5][3] = 1

g1.graph[6][4] = 1
g1.graph[6][8] = 1

g1.graph[7][4] = 1
g1.graph[7][8] = 1

g1.graph[8][6] = 1
g1.graph[8][7] = 1



print('G1 non direction graph')


for row in range(9):
    for col in range(9):
        print(g1.graph[row][col], end=' ')
    print()


current = 0
stack.append(current)
visited_array.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(9):
        if g1.graph[current][vertex] == 1:
            if vertex in visited_array:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visited_array.append(current)
    else:
        current = stack.pop()


print('Visited set -->', end='')
for i in visited_array:
    print(chr(ord('A')+i), end='   ')
