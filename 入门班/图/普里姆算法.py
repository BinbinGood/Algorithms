
import heapq
# 输入一个图，输出最短路径的边
# hashset存放考察过的点集
# queue存放解锁的边
# result存放结果的边

# 1，随机挑选一个点开始，若该点不在hashset中，则将其放入hashset中。同时将该点所有的edges放入queue中
# 2，依次弹出queue中的最小边，如果此边指向的点不在hashset中，则将其放入result和hashset中，同时将该点指向的边全部放入queue中
# 3，重复步骤二，queue为空时结束循环

def Prim(graph):
    hashset = set()
    result = set()
    queue = []
    for node in graph.nodes.values():
        if node not in hashset:
            hashset.add(node)
            for edge in node.edges:
                heapq.heappush(queue, edge)
            while queue:
                edge = heapq.heappop(queue)
                tonode = edge.tonode
                if tonode not in hashset:  # hashset中不包含此点，表示是新的点。
                    hashset.add(tonode)
                    result.add(edge)
                    for nextedge in tonode.edges:  # 同时要将此点指向的边全部放入队列中
                        heapq.heappush(queue, nextedge)
    return result
