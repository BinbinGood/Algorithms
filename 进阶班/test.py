class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleList():
    def __init__(self):
        self.head = None


def Fanzhuan(head):
    if head is None:
        return
    pre, cur = None, head
    while cur:
        tem = cur.next
        cur.next = pre
        pre = cur
        cur = tem
    return pre


def PrintList(head):
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next


if __name__ == "__main__":
    # list1 = SingleList()
    # list1.head = Node(1)
    # list1.head.next = Node(2)
    # list1.head.next.next = Node(3)
    #
    # PrintList(list1.head)
    # list2head = Fanzhuan(list1.head)
    # print("-----")
    # PrintList(list2head)
    a = 2
    b = 1
    print(a if a == 0 else b)
    dp = [[-1] * 5 for _ in range(4)]
    print(len(dp))
