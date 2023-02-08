# Chapter 9 minimum spanning tree
# low cost weight graph for clear snow and make a way
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE):
            print("%2d" % g.graph[row][col], end=' ')
        print()
    print()


def findVertex(g, findVtx):
    stack = []
    visitedAry = []  # 방문한 노드

    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                    pass
                else:  # 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break

        if next != None:  # 다음에 방문할 정점이 있는 경우
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:  # 다음에 방문할 정점이 없는 경우
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False


## 전역 변수 선언 부분 ##
g = None
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산']
Seoul, Ulaanbaatar, Beijin, Moscow, Tokyo, Bangkok = 0, 1, 2, 3, 4, 5

## 메인 코드 부분 ##
gSize = 6
g = Graph(gSize)
g.graph[Seoul][Ulaanbaatar] = 1
g.graph[Seoul][Beijin] = 2
g.graph[Ulaanbaatar][Seoul] = 1
g.graph[Ulaanbaatar][Beijin] = 4
g.graph[Ulaanbaatar][Moscow] = 3
g.graph[Ulaanbaatar][Tokyo] = 6
g.graph[Beijin][Seoul] = 2
g.graph[Beijin][Ulaanbaatar] = 4
g.graph[Beijin][Moscow] = 5
g.graph[Moscow][Ulaanbaatar] = 3
g.graph[Moscow][Beijin] = 5
g.graph[Moscow][Tokyo] = 8
g.graph[Moscow][Bangkok] = 9
g.graph[Tokyo][Ulaanbaatar] = 6
g.graph[Tokyo][Moscow] = 8
g.graph[Tokyo][Bangkok] = 9
g.graph[Bangkok][Moscow] = 9
g.graph[Bangkok][Tokyo] = 8

print('===== Whole map =====')
printGraph(g)

# egde making
edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if g.graph[i][k] != 0:
            edgeAry.append([g.graph[i][k], i, k])

from operator import itemgetter

edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True)

new_array = []
for i in range(0, len(edgeAry), 2):
    new_array.append(edgeAry[i])

index = 0
while len(new_array) > gSize - 1:  # until egde is -1 repeat
    start = new_array[index][1]
    end = new_array[index][2]
    saveCost = new_array[index][0]

    g.graph[start][end] = 0
    g.graph[end][start] = 0

    startYN = findVertex(g, start)
    endYN = findVertex(g, end)

    if startYN and endYN:
        del (new_array[index])
    else:
        g.graph[start][end] = saveCost
        g.graph[end][start] = saveCost
        index += 1

print('Low cost map')
printGraph(g)
