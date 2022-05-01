# 问题描述；打印两个有序链表的公共部分
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleList(object):
    def __init__(self):
        self.head = None


def PrintCommonPart(head1, head2):
    list1, list2 = head1, head2
    while list1 and list2:
        if list1.value < list2.value:
            list1 = list1.next
        elif list1.value > list2.value:
            list2 = list2.next
        else:
            print(list1.value)
            list1 = list1.next
            list2 = list2.next


if __name__ == "__main__":
    # 创建链表
    list1 = SingleList()
    list1.head = Node(1)
    list1.head.next = Node(3)
    list1.head.next.next = Node(3)
    list1.head.next.next.next = Node(5)
    list1.head.next.next.next.next = Node(5)
    list1.head.next.next.next.next.next = Node(8)
    list1.head.next.next.next.next.next.next = Node(9)
    list1.head.next.next.next.next.next.next.next = Node(9)

    list2 = SingleList()
    list2.head = Node(0)
    list2.head.next = Node(3)
    list2.head.next.next = Node(5)
    list2.head.next.next.next = Node(5)
    list2.head.next.next.next.next = Node(6)
    list2.head.next.next.next.next.next = Node(8)
    list2.head.next.next.next.next.next.next = Node(9)

    PrintCommonPart(list1.head, list2.head)
