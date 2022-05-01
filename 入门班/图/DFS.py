def DFS(node):
    if node is None:
        return
    stack = [node]
    set = {node}
    print(node.value)
    while stack:
        node = stack.pop()
        for i in node.nexts:  # 遍历node的后续节点
            if i not in set:  # 如果当前节点没有遇到过，则将node和该节点都入栈
                stack.append(node)
                stack.append(i)
                set.add(i)
                print(i.value) # 处理的位置
                break
