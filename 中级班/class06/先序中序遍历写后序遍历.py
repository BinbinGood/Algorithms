# 已知一棵二叉树中没有重复节点，并且给定了这棵树的中序遍历数组和先序遍历
# 数组，返回后序遍历数组。
# 比如给定：
# int[] pre = { 1, 2, 4, 5, 3, 6, 7 };
# int[] in = { 4, 2, 5, 1, 6, 3, 7 };
# 返回：
# {4,5,2,6,7,3,1}

def prein2pos(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return

    n = len(preorder)
    posorder = [0] * n

    process(preorder, inorder, posorder, 0, n - 1, 0, n - 1, 0, n - 1)
    return posorder


def process(preorder, inorder, posorder, prei, prej, ini, inj, posi, posj):
    if prei > prej:
        return
    if prei == prej:
        posorder[posj] = preorder[prei]
        return

    posorder[posj] = preorder[prei]
    find = ini
    for find in range(ini, inj + 1, 1):  # 这个地方可以做一些优化，使用哈希表存储中序遍历每个元素和它对应的位置索引。
        if inorder[find] == preorder[prei]:  # 这样就避免了循环遍历查找元素的位置
            break
    process(preorder, inorder, posorder, prei + 1, prei + find - ini, ini, find - 1, posi, posi + find - ini - 1)
    process(preorder, inorder, posorder, prei + find - ini + 1, prej, find + 1, inj, posi + find - ini, posj - 1)


pre = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
print(prein2pos(pre, inorder))
