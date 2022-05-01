
class Graph():
    def __init__(self):
        self.nodes = {}
        self.edges = set()


class Node():
    def __init__(self, value, ins=0, outs=0):
        self.value = value
        self.ins = ins
        self.outs = outs
        self.nexts = []
        self.edges = []


class Edge():
    def __init__(self, weight, fromnode, tonode):
        self.weight = weight
        self.formnode = fromnode
        self.tonode = tonode

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

    graphmatrix = [[0, 3, 2],
                   [2, 0, 5],
                   [1, 0, 3],
                   [2, 1, 2],
                   [1, 2, 7]]

    graph1 = createGraph(graphmatrix)
    print([graph1.nodes[1].edges[i].weight for i in range(len(graph1.nodes[1].edges))])
    # print([i.value for i in graph1.nodes])
