# Chapter 4
# Graph

class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


g1 = graph(4)
g1.graph[0][1] = 1
g1.graph[0][2] = 1
g1.graph[0][3] = 1

g1.graph[1][0] = 1
g1.graph[1][2] = 1
g1.graph[1][3] = 1

g1.graph[2][0] = 1
g1.graph[2][1] = 1
g1.graph[2][3] = 1

g1.graph[3][0] = 1
g1.graph[3][2] = 1

print('Non direction graph g1')
for row in range(4):
    for col in range(4):
        print(g1.graph[row][col], end=' ')
    print()

# g2 example without looking
g2 = graph(4)
g2.graph[0][3] = 1
g2.graph[1][2] = 1
g2.graph[1][3] = 1
g2.graph[3][0] = 1
g2.graph[3][1] = 1
g2.graph[2][1] = 1

print('Example')
for row in range(4):
    for col in range(4):
        print(g2.graph[row][col], end=' ')
    print()
