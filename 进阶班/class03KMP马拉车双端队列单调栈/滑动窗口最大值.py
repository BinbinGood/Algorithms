# 双端队列的几种操作
class WindowMax():
    def __init__(self, a):
        self.arr = a
        self.L = -1
        self.R = 0
        self.qmax = []

    def addNumFormRight(self):
        if self.R == len(self.arr):
            return
        while (self.qmax) and (self.arr[self.qmax[-1]] <= self.arr[self.R]):
            self.qmax.pop()
        self.qmax.append(self.R)
        self.R += 1

    def removeNumFromLeft(self):
        if self.L > self.R - 1:
            return
        self.L += 1
        if (self.qmax[0] == self.L):
            self.qmax.pop(0)

    def getMax(self):
        if self.qmax:
            return self.arr[self.qmax[0]]
        return None


# 针对此题目，具体的实现
# 如果数组长度为n，窗口大小为w，则一共产生n-w+1个窗口的最大值。
# 请实现一个函数。 输入:整型数组arr，窗口大小为w。
# 输出:一个长度为n-w+1的数组res，res[i]表示每一种窗口状态下的
def getMaxWindow(arr, w):
    if (len(arr) < w) or (arr is None) or (w < 1):
        return None
    # 定义一个双端队列
    qmax = []
    res = []
    for i in range(len(arr)):
        # 从右边添加元素
        while qmax and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        qmax.append(i)
        # 从左边删除元素
        if qmax[0] == i - w:
            qmax.pop(0)
        if i >= w - 1:  # 窗口形成了
            res.append(arr[qmax[0]])
    return res


if __name__ == "__main__":
    str1 = [4, 3, 5, 4, 3, 3, 6, 7]
    print(getMaxWindow(str1, 3))
