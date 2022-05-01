class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleList(object):
    def __init__(self):
        self.head = None


def isPalindrome1(head):
    # 方法1：使用堆栈，全压栈然后出栈
    cur = head
    stack = []
    while cur:
        stack.append(cur.value)
        cur = cur.next
    cur = head
    while cur:
        if stack.pop() != cur.value:
            return False
        cur = cur.next
    return True


def isPalindrome2(head):
    # 方法2：使用快慢指针，将后半个链表压栈，然后依次弹栈比较
    slow = head.next  # 此处和方法3不同，这里的慢指针先走一步，这样可以保证最终慢指针指向链表的右半部分。
    fast = head  # 偶数是指向两个中间节点右边的节点，奇数时指向中间节点的下一个节点
    while fast.next and fast.next.next:  # 判断条件必须这样写！！！
        slow = slow.next
        fast = fast.next.next
    stack = []
    while slow:
        stack.append(slow.value)
        slow = slow.next
    cur = head
    while stack:
        if stack.pop() != cur.value:
            return False
        cur = cur.next
    return True


def isPalindrome3(head):
    # 方法3：使用快慢指针。额外空间复杂度为O(1)
    slow = head
    fast = head
    while fast.next and fast.next.next:
        # 经过此循环，快指针走到结尾，慢指针走到中间。
        # 注意！！！奇数和偶数长度使慢指针走到的地方不同
        # 此时保证链表使奇数时指向中间节点，偶数时指向中间两个节点左边的那个节点
        slow = slow.next
        fast = fast.next.next
    # 反转右半部分链表
    fast = slow.next
    slow.next = None  # 将中间节点指向None
    while fast:
        # 经过此循环，slow代表最右边的节点
        tem = fast.next
        fast.next = slow
        slow = fast
        fast = tem
    tem = slow  # 将最后节点保存下来，最后恢复链表使用
    fast = head  # 指向链表头
    succeed = True
    while slow and fast:
        if slow.value != fast.value:
            succeed = False
            break
        slow = slow.next
        fast = fast.next
    # 将链表恢复
    slow = tem.next
    tem.next = None
    while slow:
        fast = slow.next
        slow.next = tem
        tem = slow
        slow = fast
    return succeed


if __name__ == "__main__":
    # 创建链表
    linklist = SingleList()
    linklist.head = Node(1)
    linklist.head.next = Node(2)
    linklist.head.next.next = Node(3)
    linklist.head.next.next.next = Node(4)
    linklist.head.next.next.next.next = Node(6)
    linklist.head.next.next.next.next.next = Node(4)
    linklist.head.next.next.next.next.next.next = Node(3)
    linklist.head.next.next.next.next.next.next.next = Node(2)
    linklist.head.next.next.next.next.next.next.next.next = Node(1)

    # isPalindrome1(linklist.head)
    # isPalindrome2(linklist.head)
    print(isPalindrome3(linklist.head))



