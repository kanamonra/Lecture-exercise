# Chapter 4
# Graph BFS - using deque([])
from collections import deque


class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


# making g1 and give data
g = None
# queue = []
queue = deque([])
visited_array = []

# main section
SIZE = 4
g = graph(SIZE)

g.graph[0][3] = 1
g.graph[1][2] = 1
g.graph[1][3] = 1
g.graph[3][0] = 1
g.graph[3][1] = 1
g.graph[2][1] = 1

current = 0
queue.append(current)
visited_array.append(current)

while len(queue) != 0:
    n = None
    for vertex in range(4):
        if g.graph[current][vertex] == 1:
            if vertex in visited_array:
                pass
            else:
                n = vertex
                break

    if n is not None:
        current = n
        queue.append(current)
        visited_array.append(current)
    else:
        current = queue.popleft()

for i in visited_array:
    print(i, end=' --> ')
print('DONE!')
