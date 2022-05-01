# 使用队列和set集合
# 从源节点开始依次按照宽度进队列，然后弹出
# 每弹出一个点，把该点所有没有进过队列的邻接点放入队列
# 知道队列为空
from collections import deque


def BFS(node):
    if node is None:
        return
    queue = [node]  # 这里要注意，使用list效果不好。针对大量数据处理起来特别慢，要用双端队列deque
    set = {node}
    while queue:
        node = queue.pop(0)  # 对应的方法有popleft()
        print(node.value)  # 此处为处理或打印的地方
        for i in node.nexts:
            if i not in set:  # 防止有环
                queue.append(i)
                set.add(i)
