# 如何仅用队列结构实现栈结构?
# 如何仅用栈结构实现队列结构?

class queue2stack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, s):
        if len(self.queue1) == 0:
            self.queue2.append(s)
        else:
            self.queue1.append(s)

    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return
        if len(self.queue1) == 0:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)
        else:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)

    def getpeek(self):  # 获取栈顶元素
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return
        if len(self.queue1) == 0:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            num = self.queue2.pop(0)
            self.queue1.append(num)
            return num
        else:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            num = self.queue1.pop(0)
            self.queue2.append(num)
            return num


class stack2queue:
    def __init__(self):
        self.pushstack = []
        self.popstack = []

    def push(self, s):
        self.pushstack.append(s)
        self.dao()

    def pop(self):
        if len(self.popstack) == 0 and len(self.pushstack) == 0:
            return

        if len(self.popstack):
            self.dao()
            return self.popstack.pop()
        else:
            return self.popstack.pop()

    def getfirst(self):  # 获取第一个进入队列的元素
        if len(self.popstack) == 0 and len(self.pushstack) == 0:
            return

        if len(self.popstack) == 0:
            self.dao()
            return self.popstack[-1]
        else:
            return self.popstack[-1]

    def dao(self):
        if len(self.popstack) == 0:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())


if __name__ == "__main__":
    print("-------用队列实现栈--------")
    stack1 = queue2stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print(stack1.pop())
    print(stack1.getpeek())
    print("-------用栈实现队列--------")
    queue1 = stack2queue()
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    print(queue1.pop())
    print(queue1.getfirst())
