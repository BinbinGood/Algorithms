# 数组异或和的定义:把数组中所有的数异或起来得到的值
# 给定一个整型数组 arr，其中可能有正、有负、有零，求其中子数组的最大异或和
# 【举例】
# arr = {3}
# 数组只有1个数，所以只有一个子数组，就是这个数组本身，最大异或和为3
# arr = {3, -28, -29, 2}
# 子数组有很多，但是{-28, -29}这个子数组的异或和为7，是所有子数组中最大的
import random


class Node:
    def __init__(self):
        self.nexts = [None, None]  # 节点属性，右两条分支，分别表示0和1


# 把所有前缀异或和，加入到NumTrie,并按照前缀树组织
class NumTrie:
    def __init__(self):
        self.head = Node()

    def add(self, num):
        cur = self.head
        for move in range(31, -1, -1):  # move表示向右移多少位
            path = (num >> move) & 1
            cur.nexts[path] = Node() if (cur.nexts[path] is None) else (cur.nexts[path])
            cur = cur.nexts[path]

    # num最希望到的路径，最大的异或结果返回O（32）
    def maxXOR(self, num):
        cur = self.head
        res = 0
        for move in range(31, -1, -1):
            # 当前位如果是1，path就是整数1
            # 当前位如果是0，path就是整数0
            path = (num >> move) & 1  # num第move位置上的状态提取出来
            # sum该位的状态，最期待的路，符号位希望遇到同号的数
            best = path if move == 31 else path ^ 1
            # best：最期待的路可以走就走，不可以走就走另一条路->实际走的路
            best = best if (cur.nexts[best] is not None) else (best ^ 1)
            # path num第move位的状态，best是根据path实际走的路
            res |= (path ^ best) << move
            cur = cur.nexts[best]
        return res


def maxXORSurray(arr):
    if (arr is None) or len(arr) == 0:
        return 0
    maxres = arr[0]  # 系统最小值
    xor = 0  # 初始状态，异或和为0
    numtrie = NumTrie()
    numtrie.add(0)
    for i in range(len(arr)):
        xor ^= arr[i]
        # numtrie装着0~0,0~1,.....0~i-1的异或和
        temp = numtrie.maxXOR(xor)
        # 因为python中，整数不是32位保存的，所以按照32位整数，计算得到的最大异或和需要判断负数的情况
        if (temp & (1 << 31)):  # 取符号位，若为1 ，表示为负数
            temp &= 0x6fffffff  # 将最高位的负数去掉
            temp = -temp  # 从新添加符号

        maxres = max(maxres, temp)
        numtrie.add(xor)
    return maxres


# 对数器
def comparator(arr):
    if len(arr) == 0:
        return 0
    maxres = arr[0]
    for i in range(len(arr)):
        eor = 0
        for j in range(i, len(arr)):
            eor ^= arr[j]
            maxres = max(maxres, eor)
    return maxres


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    arr = [3, -28, -29, 2]  # 此方法针
    res = maxXORSurray(arr)
    print(res)
    # print("----------------比较器---------------")
    # for _ in range(100000):
    #     arr = generateArray(10, -10, 50)
    #     res = maxXORSurray(arr)
    #     comp = comparator(arr)
    #     if res != comp:
    #         print("error")
    #         print(arr)
    #         print(res)
    #         print(comp)
    #         break
    # print("success!")
    for i in range(-100, -1):
        for j in range(-100, -1):
            if i ^ j < 0:
                print(i)
                print(j)
                break
