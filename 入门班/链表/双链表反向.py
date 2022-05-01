class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None


class DoubleList(object):
    def __init__(self):
        self.head = None


def ReverseList(head):
    cur, pre = head, None
    while cur:
        tem = cur.next
        cur.next = pre
        cur.pre = tem
        pre = cur
        cur = tem
    return pre


def PrintList(head):
    cur, end = head, None
    print("正向打印:")
    while cur:
        print(cur.value)
        end = cur
        cur = cur.next
    print("反向打印:")
    while end:
        print(end.value)
        end = end.pre


if __name__ == "__main__":
    list1 = DoubleList()
    list1.head = Node(1)
    list1.head.next = Node(2)
    list1.head.next.pre = list1.head
    list1.head.next.next = Node(3)
    list1.head.next.next.pre = list1.head.next
    list1.head.next.next.next = Node(4)
    list1.head.next.next.next.pre = list1.head.next.next
    print("-------------原始链表--------------")
    PrintList(list1.head)
    list1.head = ReverseList(list1.head)
    print("------------反转后链表--------------")
    PrintList(list1.head)