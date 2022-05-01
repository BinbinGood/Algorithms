# 请编写一个程序，对一个栈里的整型数据，按升序进行排序（即排序前，栈里
# 的数据是无序的，排序后最大元素位于栈顶），要求最多只能使用一个额外的
# 栈存放临时数据，但不得将元素复制到别的数据结构中。
def Sortstack(stack):
    helpstack = []
    while stack:
        num = stack.pop()
        if len(helpstack) == 0:
            helpstack.append(num)
        elif helpstack[-1] >= num:  # 栈顶元素大于等num
            helpstack.append(num)
        else:  # 栈顶元素小于num
            while len(helpstack) != 0 and helpstack[-1] < num:
                stack.append(helpstack.pop())
            helpstack.append(num)
    while helpstack:
        stack.append(helpstack.pop())


if __name__ == "__main__":
    stack1 = [4, 8, 3, 5, 2, 9, 1, 7, 7]
    Sortstack(stack1)
    print(stack1)
