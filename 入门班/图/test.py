from 宽度优先遍历 import BFS
from DFS import DFS
from 拓扑排序 import sortedTopology
from 克鲁斯卡算法 import kruskalMST
from 普里姆算法 import Prim
from 迪克斯特拉算法 import Dijkstra2


class Graph:
    def __init__(self):
        self.nodes = {}  # 存放每一个节点的名字和其对应的节点
        self.edges = set()  # 是一个集合类型，保存边


class Node:
    def __init__(self, value, ins=0, outs=0):
        self.value = value
        self.ins = ins
        self.outs = outs
        self.nexts = []
        self.edges = []


class Edge:
    def __init__(self, weight, fromnode, tonode):
        self.weight = weight
        self.fromnode = fromnode
        self.tonode = tonode

    def __lt__(self, other):
        return self.weight < other.weight


# 接口函数，根据具体题目给出的数据格式转化为我们熟悉的格式。然后利用熟悉格式的算法进行解题
# 输入矩阵N*3形状的
# 每一行表示一条边，[0]位置表示起点，[1]表示终点，[2]表示权重
def createGraph(matrix):
    graph = Graph()
    for i in range(len(matrix)):
        fromname = matrix[i][0]
        toname = matrix[i][1]
        weight = matrix[i][2]
        if fromname not in graph.nodes:
            graph.nodes[fromname] = Node(fromname)
        if toname not in graph.nodes:
            graph.nodes[toname] = Node(toname)
        fromnode = graph.nodes[fromname]
        tonode = graph.nodes[toname]
        newedge = Edge(weight, fromnode, tonode)
        fromnode.nexts.append(tonode)
        fromnode.outs += 1
        tonode.ins += 1
        fromnode.edges.append(newedge)
        graph.edges.add(newedge)
    return graph


if __name__ == "__main__":
    print("------宽度优先遍历测试-------")
    graphmatrix = [[0, 3, 2],
                   [3, 0, 2],
                   [2, 0, 5],
                   [0, 2, 5],
                   [1, 0, 3],
                   [0, 1, 3],
                   [2, 1, 2],
                   [1, 2, 2]]
    graph1 = createGraph(graphmatrix)  # 无向图
    BFS(graph1.nodes[1])
    print("-------深度(广度)优先遍历测试--------")
    graphmatrix2 = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 3, 1],
                    [3, 1, 1],
                    [1, 5, 1],
                    [5, 1, 1],
                    [2, 4, 1],
                    [4, 2, 1],
                    [2, 3, 1],
                    [3, 2, 1],
                    [2, 5, 1],
                    [5, 2, 1],
                    [4, 3, 1],
                    [3, 4, 1],
                    [4, 5, 1],
                    [5, 4, 1]]
    graph2 = createGraph(graphmatrix2)  # 无向图
    DFS(graph2.nodes[3])
    # print("------宽度优先遍历测试-------")
    # BFS(graph2.nodes[4])
    print("-------拓扑排序测试-------")
    graphmatrix3 = [[1, 2, 1],
                    [1, 3, 1],
                    [2, 3, 1],
                    [2, 4, 1],
                    [3, 4, 1]]
    graph3 = createGraph(graphmatrix3)
    nodes = sortedTopology(graph3)
    print([node.value for node in nodes])
    print("-------K算法测试-------")
    graphmatrix4 = [[1, 2, 3],
                    [2, 1, 3],
                    [1, 3, 100],
                    [3, 1, 100],
                    [1, 4, 7],
                    [4, 1, 7],
                    [2, 3, 5],
                    [3, 2, 5],
                    [2, 4, 2],
                    [4, 2, 2],
                    [4, 3, 10000],
                    [3, 4, 10000]]
    graph4 = createGraph(graphmatrix4)
    edges = kruskalMST(graph4)
    print([edge.weight for edge in edges])
    print("-------P算法测试-------")
    edgesp = Prim(graph4)
    print([edge.weight for edge in edgesp])
    print("-------迪克斯塔拉算法测试-------")
    graphmatrix5 = [[1, 2, 3],
                    [2, 1, 3],
                    [1, 3, 15],
                    [3, 1, 15],
                    [1, 4, 9],
                    [4, 1, 9],
                    [2, 3, 2],
                    [3, 2, 2],
                    [4, 3, 7],
                    [3, 4, 7],
                    [2, 5, 200],
                    [5, 2, 200],
                    [5, 3, 14],
                    [3, 5, 14],
                    [4, 5, 16],
                    [5, 4, 16]]
    graph5 = createGraph(graphmatrix5)
    distancemap = Dijkstra2(graph5.nodes[1],5)
    print("正确值:0,3,5,9,19")
    print([distance for distance in distancemap.values()])
