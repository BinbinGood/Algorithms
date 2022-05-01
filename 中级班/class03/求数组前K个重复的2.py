# 给定一个字符串类型的数组arr，求其中出现次数最多的前K个
# 此外还要求可以动态调整，可是随时使用add()和PrintTopk()两种操作。

class Node:
    def __init__(self, s, times):
        self.s = s
        self.times = times


class TopK:
    def __init__(self, k):
        self.strnumhash = dict()  # 存放字符和其对应的词频
        self.littleheap = [None] * k  # 存放当前词频的前k个字符和其对应的词频
        self.indexhash = dict()  # 存放每个字符在小根堆中的位置索引
        self.index = 0  # 记录当前小根堆已经存放的元素个数
        self.k = k

    def add(self, str):
        preindex = -1
        if str not in self.strnumhash:  # 字符第一次出现
            curnode = Node(str, 1)
            self.strnumhash[str] = curnode
            self.indexhash[curnode] = -1
        else:
            curnode = self.strnumhash[str]
            curnode.times += 1
            preindex = self.indexhash[curnode]
        if preindex == -1:  # 当前字符串不在小根堆中
            if len(self.littleheap) == self.index:  # 堆满了
                if self.littleheap[0].times < curnode.times:
                    self.indexhash[self.littleheap[0]] = -1
                    self.indexhash[curnode] = 0
                    self.littleheap[0] = curnode
                    self.heapify(0, self.index)
            else:  # 堆未满，将当前节点加入堆中
                self.indexhash[curnode] = self.index  #
                self.littleheap[self.index] = curnode
                self.heapInsert(self.index)
                self.index += 1
        else:  # 当前字符在小根堆中，利用heapify向上调整
            self.heapify(preindex, self.index)

    def PrintTopk(self):
        print(f"Top{self.k}:")
        for i in range(self.index):
            print(f"字符串：{self.littleheap[i].s}，词频为：{self.littleheap[i].times}")

    # 向上调整
    def heapInsert(self, i):
        while self.littleheap[i].times < self.littleheap[int((i - 1) / 2)].times:
            self.swap(i, int((i - 1) / 2))
            i = int((i - 1) / 2)

    # 向下调整
    def heapify(self, i, size):
        left = 2 * i + 1
        while left < size:
            if left + 1 < size and self.littleheap[left + 1].times < self.littleheap[left].times:
                littlest = left + 1
            else:
                littlest = left
            if self.littleheap[i].times <= self.littleheap[littlest].times:  # 如果,则跳出循环
                break
            self.swap(i, littlest)
            i = littlest
            left = 2 * i + 1

    def swap(self, a, b):  # 不仅在堆中位置交换，在哈希表中也要修改相应的位置索引
        self.indexhash[self.littleheap[a]] = b
        self.indexhash[self.littleheap[b]] = a
        tem = self.littleheap[a]
        self.littleheap[a] = self.littleheap[b]
        self.littleheap[b] = tem


if __name__ == "__main__":
    str1 = ['a', 'b', 'c', 'a', 'b', 'a', 'a', 'b', 'd', 'e', 'b', 'c', 'g', 'c', 'e', 'h', 'g']
    k = 1
    top = TopK(k)
    for i in str1:
        top.add(i)
    top.PrintTopk()
    top.add('b')
    top.PrintTopk()
