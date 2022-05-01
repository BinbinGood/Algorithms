# 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素
# 的操作。
# 要求：1.pop、push、getMin操作的时间复杂度都是O(1)；2.设计的栈类型可以
# 使用现成的栈结构

class Minelement:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, s):
        self.stack.append(s)
        if len(self.minstack) == 0:
            self.minstack.append(s)
        else:
            num = self.minstack[-1]  # 获取栈顶元素的值
            if s < num:
                self.minstack.append(s)
            else:
                self.minstack.append(num)

    def pop(self):
        if len(self.stack) == 0:
            return
        self.minstack.pop()
        return self.stack.pop()

    def getMin(self):
        if len(self.stack) == 0:
            return
        return self.minstack[-1]


if __name__ == "__main__":
    stack1 = Minelement()
    stack1.push(2)
    stack1.push(3)
    stack1.push(1)
    stack1.push(5)
    print(stack1.getMin())
    stack1.pop()
    print(stack1.getMin())
    stack1.pop()
    print(stack1.getMin())
