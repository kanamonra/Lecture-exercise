# Chapter 4
# Graph for friends that has ...

class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print('', end='')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end=' ')
        print()
    print()


# making g1 and give data
g1 = None
nameAry = ['Mon', 'Cha', 'Rac', 'Joy', 'Pho', 'Ros']
Monica, Chandler, Rachel, Joy, Phoebe, Rose = 0, 1, 2, 3, 4, 5
stack = []
visitedAry = []

# main section
gSize = 6
g1 = graph(gSize)

g1.graph[Monica][Chandler] = 1
g1.graph[Monica][Rachel] = 1
g1.graph[Chandler][Monica] = 1
g1.graph[Chandler][Joy] = 1
g1.graph[Rachel][Monica] = 1
g1.graph[Rachel][Joy] = 1
g1.graph[Joy][Chandler] = 1
g1.graph[Joy][Rachel] = 1
g1.graph[Joy][Phoebe] = 1
g1.graph[Joy][Rose] = 1
g1.graph[Phoebe][Joy] = 1
g1.graph[Phoebe][Rose] = 1
g1.graph[Rose][Joy] = 1
g1.graph[Rose][Phoebe] = 1

print('G1 non direction graph')


for row in range(4):
    for col in range(4):
        print(g1.graph[row][col], end=' ')
    print()

print_graph(g1)
current = 0		# 시작 정점 A
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(4):
        if g1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()


print('Visited set -->', end='')
for i in visitedAry:
    print(i, end='   ')
