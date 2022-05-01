# 输入给定出发点
# 输出该点到所有点的最短距离

# 原始的递归的方式
def Dijkstra(head):
    hashdistance = {head: 0}  # 存放所有节点到head节点的距离，其中的值会动态更新
    selectednodes = set()  # 存放已经使用过的节点
    mininode = getMinDistanceAndUnselectedNode(hashdistance, selectednodes)
    while mininode:
        distance = hashdistance[mininode]
        for edge in mininode.edges:
            tonode = edge.tonode
            if tonode not in hashdistance:
                hashdistance[tonode] = distance + edge.weight
            else:
                hashdistance[tonode] = min(hashdistance[tonode], distance + edge.weight)
        # 使用过的节点放入selectnodes中，重新选择下次要使用的最小距离的节点
        selectednodes.add(mininode)
        mininode = getMinDistanceAndUnselectedNode(hashdistance, selectednodes)
    return hashdistance


# 从哈希距离表中选出不包含torchnode的最短距离的节点，
def getMinDistanceAndUnselectedNode(heashdistance, torchnode):
    mininode = None
    minidistance = 10000000  # 假设距离不超过10000000
    # 遍历找出距离最小的
    for node in heashdistance.keys():
        distance = heashdistance[node]
        if (node not in torchnode) and (distance < minidistance):
            mininode = node
            minidistance = distance
    return mininode


# 使用堆改写，利用堆结构找到距离最小的节点。优化了遍历的时间
class NodeHeap():
    def __init__(self, size):
        self.nodes = [None] * size
        self.hashindex = {}
        self.hashdiztance = {}
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addOrUpdateOrIgnore(self, node, distance):
        if self.inHeap(node):
            self.hashdiztance[node] = min(self.hashdiztance[node], distance)
            # 因为距离只可能更新变小，所以只需要向上调整即可
            self.HeapInsert(node, self.hashindex[node])
        if self.isEntered(node) is False:
            self.nodes[self.size] = node
            self.hashindex[node] = self.size
            self.hashdiztance[node] = distance
            self.HeapInsert(node, self.size)
            self.size += 1

    def pop(self):
        result = [self.nodes[0], self.hashdiztance[self.nodes[0]]]
        self.size -= 1
        self.swap(0,self.size)
        self.hashindex[self.nodes[self.size]] = -1
        del self.hashdiztance[self.nodes[self.size]]
        self.nodes[self.size] = None
        self.Heapify(0,self.size)
        return result

    # 输入：节点和其对应的位置索引
    # 向上调整
    def HeapInsert(self, node, index):
        while self.hashdiztance[node] < self.hashdiztance[self.nodes[int((index - 1) / 2)]]:
            self.swap(index, int((index - 1) / 2))
            index = int((index - 1) / 2)

    def Heapify(self, index, size):
        left = index * 2 + 1
        while left < size:
            # 在保证左右子节点不越界的情况下，找到两个子节点的最小值,若有右节点则判断右节点是否为最小值
            if left + 1 < size and self.hashdiztance[self.nodes[left + 1]] < self.hashdiztance[self.nodes[left]]:
                smallest = left + 1
            else:
                smallest = left
                # 如果小于该位置的值，则跳出循环
            if self.hashdiztance[self.nodes[index]] <= self.hashdiztance[self.nodes[smallest]]:
                break
            # 否则交换位置，继续往下比较
            self.swap(index, smallest)
            index = smallest
            left = 2 * index + 1

    # 表示进过堆中，可能已经弹出
    def isEntered(self, node):
        return node in self.hashindex

    # 表示在堆中
    def inHeap(self, node):
        return self.isEntered(node) and (self.hashindex[node] != -1)

    # 交换两个节点的位置，输入为两个节点在nodes中的的位置索引
    def swap(self, index1, index2):
        # 哈希表修改
        self.hashindex[self.nodes[index1]] = index2
        self.hashindex[self.nodes[index2]] = index1
        # nodes中修改
        temp = self.nodes[index1]
        self.nodes[index1] = self.nodes[index2]
        self.nodes[index2] = temp


def Dijkstra2(head, size):
    heap = NodeHeap(size)
    heap.addOrUpdateOrIgnore(head,0)
    result = {}
    while heap.isEmpty() is False:
        record = heap.pop()
        for edge in record[0].edges:
            heap.addOrUpdateOrIgnore(edge.tonode, edge.weight+record[1])
        result[record[0]] = record[1]
    return result
