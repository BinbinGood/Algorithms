# 输入一个图
# 哈希表用来保存每一个node的剩余入度
# 队列，保存入读为零的节点
# result列表，保存最终的节点顺序

# 1，遍历图的所有节点，将其对应的入度放入哈希表中，同时把遇到的入度为0的点放入队列中
# 2，将队列中的点弹出，放入result中。
# 3，同时遍历弹出的点的所有邻接点，将所有邻接点的入度减一，在此过程也要判断将入度为0的点放入队列中
# 4，直到队列为空
# 5，返回result即为拓扑循序的点集

def sortedTopology(graph):
    inhash = {}
    queue = []
    for node in graph.nodes.values():  # 此处graph.nodes是一个字典，所以使用values（）函数获取所有的节点nodes
        inhash[node] = node.ins
        if inhash[node] == 0:
            queue.append(node)
    result = []
    while queue:
        cur = queue.pop(0)
        result.append(cur)
        for node in cur.nexts:
            inhash[node] -= 1
            if inhash[node] == 0:
                queue.append(node)
    return result
