def nixuzhan(stack):
    if len(stack) == 0:
        return
    num = process(stack)  # 得到栈底元素
    nixuzhan(stack)  # 递归处理剩余部分的逆序
    stack.append(num)  # 把得到的栈底元素放入栈顶

# 该函数返回此时的栈底元素
def process(stack):
    num = stack.pop()
    if len(stack) == 0:  # base case
        return num
    else:
        last = process(stack)  # 得到剩余部分的栈底元素
        stack.append(num)  # 把弹出的元素重新入栈
        return last


if __name__ == "__main__":
    stack1 = [1, 2, 3, 4, 5]
    nixuzhan(stack1)
    print(stack1)
