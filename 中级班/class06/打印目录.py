# 给你一个字符串类型的数组arr，譬如：
# String[] arr = { "b\\cst", "d\\", "a\\d\\e", "a\\b\\c" };
# 你把这些路径中蕴含的目录结构给画出来，子目录直接列在父目录下面，并比父目录
# 向右进两格，就像这样:
# a
#   b
#     c
#   d
#     e
# b
#   cst
# d
# 同一级的需要按字母顺序排列，不能乱。

from collections import OrderedDict as od


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = dict()


# 将所有路径字符串转化为前缀树
def str2qianzuitree(arr):
    head = ListNode('')
    for i in arr:
        curstr = i.split('\\')
        cur = head
        for j in curstr:
            if j not in cur.next:
                cur.next[j] = ListNode(j)
            cur = cur.next[j]
    return head

# 打印每个节点，并且保证按照层数添加相应数量的空格
def printqianzuitree(node, level):
    if level != 0 and node.value != '':
        print(getspace(level) + node.value)
    for cur in node.next.values():
        printqianzuitree(cur, level + 1)


def getspace(level):
    res = ''
    for i in range(1, level):
        res += '  '
    return res


arr = ["b\\cst", "d\\", "a\\d\\e", "a\\b\\c"]
head = str2qianzuitree(arr)
printqianzuitree(head, 0)
