class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleList(object):
    def __init__(self):
        self.head = None


def PrintList(head):
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next


def LittleEqualBig(head, num):
    if not head:  # 判断空链表返回
        return
    cur = head
    little1, little2 = None, None
    equal1, equal2 = None, None
    big1, big2 = None, None
    while cur:
        tem = cur.next  # 保存后续节点
        cur.next = None  # 将当前节点和后续节点断开变成一个单独的节点
        if cur.value < num:
            if not little1:
                little1 = little2 = cur
            else:
                little2.next = cur
                little2 = cur
        elif cur.value == num:
            if not equal1:
                equal1 = equal2 = cur
            else:
                equal2.next = cur
                equal2 = cur
        else:
            if not big1:
                big1 = big2 = cur
            else:
                big2.next = cur
                big2 = cur
        cur = tem
    # 将得到的三段链表连接起来
    if little2:
        if equal2:
            if big2:  #
                equal2.next = big1
            little2.next = equal1
        elif big2:
            little2.next = big1
        return little1
    elif equal2:
        if big2:
            equal2.next = big1
        return equal1
    return big1


if __name__ == "__main__":
    list = SingleList()
    list.head = Node(4)
    list.head.next = Node(5)
    list.head.next.next = Node(8)
    list.head.next.next.next = Node(6)
    list.head.next.next.next.next = Node(5)
    list.head.next.next.next.next.next = Node(8)
    print("----------原始链表---------")
    PrintList(list.head)
    node = LittleEqualBig(list.head, 3)
    print("--------转换后的链表---------")
    PrintList(node)
