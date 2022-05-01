# 给定一棵二叉树的头节点head，已知所有节点的值都不一样，返回其中最大的且符
# 合搜索二叉树条件的最大拓扑结构的大小。
# 拓扑结构：不是子树，只要能连起来的结构都算。

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class record:
    def __init__(self, left, right):
        self.l = left
        self.r = right


def bstTopoSize(head):
    hashmap = dict()
    return posOrder(head, hashmap)


def posOrder(h, hashmap):
    if h is None:
        return 0
    ls = posOrder(h.left, hashmap)
    rs = posOrder(h.right, hashmap)
    modifyMap(h.left, h.value, hashmap, True)
    modifyMap(h.right, h.value, hashmap, False)
    lr = hashmap[h.left] if (h.left in hashmap) else None  # Python和JAVA不同，这里的Key不存在时会保存，但是JAVA不会保存会返回None。所以要加一个判断
    rr = hashmap[h.right] if (h.right in hashmap) else None
    lbst = 0 if (lr is None) else lr.l + lr.r + 1
    rbst = 0 if (rr is None) else rr.l + rr.r + 1
    hashmap[h] = record(lbst, rbst)
    return max(ls, max(rs, lbst + rbst + 1))


# s用来判断是前往左子树还是右子树。True表示右子树，False表示左子树
def modifyMap(n, v, hashmap, s):
    if ((n is None) or (n not in hashmap)):
        return 0
    r = hashmap[n]
    if (s and n.value > v) or ((not s) and n.value < v):
        del hashmap[n]
        return r.l + r.r + 1
    else:
        minus = modifyMap((n.right if s else n.left), v, hashmap, s)
        if s:
            r.r = r.r - minus
        else:
            r.l = r.l - minus
        hashmap[n] = r
        return minus


if __name__ == "__main__":
    head = Node(6)
    head.left = Node(1)
    head.left.left = Node(0)
    head.left.right = Node(3)
    head.right = Node(12)
    head.right.left = Node(10)
    head.right.left.left = Node(4)
    head.right.left.left.left = Node(2)
    head.right.left.left.right = Node(5)
    head.right.left.right = Node(14)
    head.right.left.right.left = Node(11)
    head.right.left.right.right = Node(15)
    head.right.right = Node(13)
    head.right.right.left = Node(20)
    head.right.right.right = Node(16)

    print(bstTopoSize(head))
