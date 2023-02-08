# 9장 응용예제 1
# 편의점 찾기
class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    global store_array
    print(' ', end='')
    for v in range(g.SIZE):
        print(store_array[v][0], end=' ')
    print()
    for row in range(g.SIZE):
        print(store_array[row][0], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end='  ')
        print()
    print()


g1 = None
store_array = [['GS25    ', 30], ['CU      ', 60], ['Seven7  ', 10], ['emart24 ', 40], ['ministop', 90]]
GS25, CU, Seven7, Emart24, ministop = 0, 1, 2, 3, 4


gSIZE = 5
g1 = graph(gSIZE)
g1.graph[0][1] = 1
g1.graph[0][2] = 1
g1.graph[1][0] = 1
g1.graph[1][2] = 1
g1.graph[1][4] = 1
g1.graph[2][1] = 1
g1.graph[2][0] = 1
g1.graph[2][4] = 1
g1.graph[3][4] = 1
g1.graph[4][1] = 1
g1.graph[4][2] = 1
g1.graph[4][3] = 1

stack = []
visited_array = []

print('Convenience store graph ฅ^•ﻌ•^ฅ')
print_graph(g1)
current = 0
most_have = current
max_count = store_array[current][1]
stack.append(current)
visited_array.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(4):
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
    if store_array[current][1] > max_count:
        max_count = store_array[current][1]
        most_have = current
    else:
        current = stack.pop()

print('Most honeychip count is -->', 'with', store_array[current][1], 'piece and\nthe STORE IS ଘ(੭˃ᴗ˂)੭ --->', store_array[current][0], end='')

