# 给定两个可能有环也可能无环的单链表，头节点head1和head2。请实
# 现一个函数，如果两个链表相交，请返回相交的 第一个节点。如果不相交，返回null
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleList(object):
    def __init__(self):
        self.head = None


# 此函数用判断链表是否是有环的，若有环返回入环的第一个节点
def IsRing(head):
    cur = head
    if not cur:
        return
    # 方法1：使用哈希表，有重复的就是有环
    # 方法2：使用快慢指针，若快指针走到NONE则无环，若走到与慢指针相等，则有环，将快指针指回链表的头，两个指针
    #       一次一步，一定会在入环节点相遇，返回此节点即可
    slow = cur.next
    fast = cur.next.next
    while slow != fast:
        if not fast.next or not fast.next.next:
            return
        slow = slow.next
        fast = fast.next.next
    fast = cur
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast


# 此函数用来判断，链表1和链表2是否相交。(可能有环)
def IsItersect(head1, head2):
    if not head1 or not head2:
        return
    cur1 = head1
    cur2 = head2
    isring1 = IsRing(cur1)
    isring2 = IsRing(cur2)
    if not isring1 and not isring2:  # 此时两者都无环
        return NoLoop(head1, head2)
    if isring1 and isring2:
        return BothLoop(head1, isring1, head2, isring2)
    return  # 当一个有环一个无环时，两个链表一定不相交


def BothLoop(head1, isring1, head2, isring2):
    if isring1 == isring2:  # 对应同样的入环节点
        cur1, cur2 = head1, head2
        len = 0
        print("两者入环节点相同")
        while cur1 != isring1:
            cur1 = cur1.next
            len += 1
        while cur2 != isring2:
            cur2 = cur2.next
            len -= 1
        if len >= 0:  # 经过此判断将长的链表放入cur1，短的链表放入cur2
            cur1 = head1
            cur2 = head2
        else:
            cur1 = head2
            cur2 = head1
            len = abs(len)
        while len:  # 长链表先走一个差值
            cur1 = cur1.next
            len -= 1
        while cur2 != cur1:  # 两个链表一快走
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur = isring1.next
        while cur != isring1:
            if cur == isring2:  # 若cur在走的过程中遇到isring2表示两个链表有不同的入环节点，返回任意一个节点
                return cur
            cur = cur.next
        return  # 若cur1在走完一周还未遇到isring2表示两者不相交


def NoLoop(head1, head2):
    cur1, cur2 = head1, head2
    len = 0
    # print("进入不是环的部分")
    while cur1.next:
        # print("进入了len+循环")
        len += 1
        cur1 = cur1.next
    while cur2.next:
        len -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return
    else:
        if len >= 0:  # 经过此判断将长的链表放入cur1，短的链表放入cur2
            cur1, cur2 = head1, head2
        else:
            cur1, cur2 = head2, head1
            len = abs(len)
        while len:  # 长链表先走一个差值
            cur1 = cur1.next
            len -= 1
        while cur1 != cur2:  # 两个链表一快走
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1


if __name__ == "__main__":
    # 创建链表1
    list1 = SingleList()
    list1.head = Node(1)
    # list1.head.next = list1.head
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(4)
    list1.head.next.next.next.next = Node(5)
    list1.head.next.next.next.next.next = list1.head.next.next.next  # 5->4

    # 创建链表2
    list2 = SingleList()
    list2.head = Node(1)
    # list1.head.next = list1.head
    list2.head.next = Node(2)
    list2.head.next.next = Node(3)
    list2.head.next.next.next = Node(4)
    list2.head.next.next.next.next = list1.head.next.next  # 4->2

    print("-------判断链表是否有环--------")
    node = IsRing(list1.head)
    if node:
        print(node.value)
    else:
        print("无环")
    print("-------处理双链表相交问题-------")
    node = IsItersect(list1.head, list2.head)
    if node:
        print(node.value)
    else:
        print("不相交")
