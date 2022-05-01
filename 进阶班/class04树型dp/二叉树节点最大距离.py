class Node():
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def maxDistance(head):
    if head is None:
        return -1
    left = process(head.left)
    right = process(head.right)
    maxdistance = max(max(left[0], right[0]), (left[1] + right[1] + 1))
    return maxdistance


# 返回类型：[距离，高度]
def process(node):
    if node is None:
        return [0, 0]
    left = process(node.left)
    right = process(node.right)
    maxdistance = max(max(left[0], right[0]), (left[1] + right[1] + 1))
    maxheight = max(left[1], right[1]) + 1
    return [maxdistance, maxheight]


if __name__ == "__main__":
    n12 = Node(12)
    n6 = Node(6)
    n5 = Node(5, n12, n6)
    n4 = Node(4, n5)
    n2 = Node(2, n4)
    n11 = Node(11)
    n9 = Node(9, None, n11)
    n8 = Node(8)
    n7 = Node(7, n8, n9)
    n10 = Node(10)
    n3 = Node(3, n10, n7)
    n1 = Node(1, n2, n3)
    headnode = n1
    print(maxDistance(headnode))
