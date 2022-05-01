# 算法描述:从小到大，依次添加边，若该边加入后会形成环，则不加此边。

# 在 Python 中，内置的标准库提供了两种实现优先队列的数据结构，分别是 heapq 模块和 PriorityQueue 模块
import heapq


class Mysets():
    def __init__(self):
        self.setMap = {}

    # 第一步将所有的点，构建自己的集合
    def Mysets(self, nodes):
        for cur in nodes:
            sets = [cur]
            self.setMap[cur] = sets

    # 判断form和to两个点所在的集合是否相同
    def isSameset(self, fromnode, tonode):
        return self.setMap[fromnode] == self.setMap[tonode]

    # 将from和to的点对应的集合进行合并
    def union(self, fromnode, tonode):
        fromset = self.setMap[fromnode]
        toset = self.setMap[tonode]
        for tonode in toset:
            fromset.append(tonode)
            self.setMap[tonode] = fromset


def kruskalMST(graph):
    pqueue = []
    mysets = Mysets()
    mysets.Mysets(graph.nodes.values())
    for edge in graph.edges:
        heapq.heappush(pqueue, edge)

    result = set()
    while pqueue:
        edge = heapq.heappop(pqueue)
        if mysets.isSameset(edge.fromnode, edge.tonode) is False:
            result.add(edge)
            mysets.union(edge.fromnode, edge.tonode)
    return result
