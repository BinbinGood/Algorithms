class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None


class SingleList(object):
    def __init__(self):
        self.head = None


def PrintList(head):
    cur = head
    print("-----next-----")
    while cur:
        print(cur.value)
        cur = cur.next
    print("-----rand------")
    cur = head
    while cur:
        if not cur.rand:
            print("-")
        else:
            print(cur.rand.value)
        cur =cur.next


def CopyList(head):
    cur = head
    while cur:  # 复制链表节点
        tem = cur.next
        cur.next = Node(cur.value)
        cur.next.next = tem
        cur = tem
    cur = head
    while cur:
        tem = cur.next
        if cur.rand:
            tem.rand = cur.rand.next
        else:
            tem.rand = None
        cur = tem.next

    res = head.next
    cur = head
    while cur:
        tem = cur.next.next
        copynode = cur.next
        cur.next = tem
        if tem:
            copynode.next = tem.next
        else:
            copynode.next = None
        cur = tem
    return res


if __name__ == "__main__":
    list1 = SingleList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(4)
    list1.head.next.next.next.next = Node(5)
    list1.head.rand = list1.head.next.next.next  # 1->4
    list1.head.next.rand = list1.head  # 2->1
    list1.head.next.next.rand = list1.head.next  # 3->2
    list1.head.next.next.next.rand = None  # 4->None
    list1.head.next.next.next.next.rand = list1.head.next.next  # 5->3
    print("--------原始链表---------")
    PrintList(list1.head)
    print("--------复制以后的链表-----")
    node = CopyList(list1.head)
    node.next.next.rand = None
    node.next.next.next.rand = node.next.next.next.next
    PrintList(node)
    print("--------原始链表---------")
    PrintList(list1.head)
