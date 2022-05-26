import random


class SegmentTree:
    def __init__(self, origin):
        # arr[]为原序列的信息从0开始，但在arr里是从1开始的
        # sum[]模拟线段树维护区间和
        # lazy[]为累加和懒惰标记
        # change[]为更新的值
        # update[]为更新慵懒标记
        MAXN = len(origin) + 1
        self.arr = [0] * MAXN  # arr[0]不用，从1开始
        for i in range(1, MAXN):
            self.arr[i] = origin[i - 1]
        self.sum = [0] * (MAXN << 2)  # 某一个范围的累加和信息
        self.lazy = [0] * (MAXN << 2)  # 某一个范围没有往下传递的累加任务
        self.change = [0] * (MAXN << 2)  # 某一个范围有没有更新操作的任务
        self.update = [False] * (MAXN << 2)  # 某一个范围更新任务，更新成什么

    def pushUp(self, rt):
        sum1 = self.sum
        sum1[rt] = sum1[rt << 1] + sum1[rt << 1 | 1]  # 当前位置的和为两个孩子的和

    # 之前的所有lazy增加和更新，从父范围发给左右两个子范围
    # 分发的策略是什么
    # ln表示左子树元素节点个数，rn表示右子树节点个数
    def pushDown(self, rt, ln, rn):
        sum1, lazy, change, update = self.sum, self.lazy, self.change, self.update
        # 先更新update和change的信息，
        # 然后更新add可能产生的懒信息。
        # 因为上次update之后可能存在add操作。反之，若存在update操作一定会把之前保存的add懒信息全部覆盖掉。
        if update[rt]:
            update[rt << 1] = True
            update[rt << 1 | 1] = True
            change[rt << 1] = change[rt]
            change[rt << 1 | 1] = change[rt]
            lazy[rt << 1] = 0
            lazy[rt << 1 | 1] = 0
            sum1[rt << 1] = change[rt] * ln
            sum1[rt << 1 | 1] = change[rt] * rn
            update[rt] = False
        if lazy[rt] != 0:
            lazy[rt << 1] += lazy[rt]
            lazy[rt << 1 | 1] += lazy[rt]
            sum1[rt << 1] += lazy[rt] * ln
            sum1[rt << 1 | 1] += lazy[rt] * rn
            lazy[rt] = 0

    # 在初始阶段，先把sum数组填好
    # 在arr[l~r]范围上，去buld，1~N
    # rt:这个范围在sum中的下标
    def build(self, l, r, rt):
        sum1, arr = self.sum, self.arr
        if l == r:
            sum1[rt] = arr[l]
            return
        mid = (l + r) >> 1
        self.build(l, mid, rt << 1)
        self.build(mid + 1, r, rt << 1 | 1)
        self.pushUp(rt)

    # L~R所有值变为C
    # l~r rt(由于self.update是一个数组，所有命名为updatefun)
    def updatefun(self, L, R, C, l, r, rt):
        sum1, lazy, change, update = self.sum, self.lazy, self.change, self.update
        if (L <= l) and (R >= r):  # 全包进去了
            update[rt] = True
            change[rt] = C
            sum1[rt] = C * (r - l + 1)
            lazy[rt] = 0
            return
        # 当前任务躲不掉，无法懒更新，要往下发
        mid = (l + r) >> 1
        self.pushDown(rt, mid - l + 1, r - mid)
        if L <= mid:
            self.updatefun(L, R, C, l, mid, rt << 1)
        if R > mid:
            self.updatefun(L, R, C, mid + 1, r, rt << 1 | 1)
        self.pushUp(rt)

    # L~R的数都加C？
    # l~r的位置rt
    def add(self, L, R, C, l, r, rt):
        sum1, lazy, change, update = self.sum, self.lazy, self.change, self.update
        if (L <= l) and (R >= r):  # 全包进去了
            sum1[rt] += C * (r - l + 1)
            lazy[rt] += C
            return
        # 任务没有把你全包
        # 要把当前任务往下发
        mid = (l + r) >> 1
        self.pushDown(rt, mid - l + 1, r - mid)
        if L <= mid:
            self.add(L, R, C, l, mid, rt << 1)
        if R > mid:
            self.add(L, R, C, mid + 1, r, rt << 1 | 1)
        self.pushUp(rt)

    # L~R的累加和是多少？
    # l~r的位置rt
    def query(self, L, R, l, r, rt):
        sum1 = self.sum
        if (L <= l) and (R >= r):
            return sum1[rt]
        mid = (l + r) >> 1
        self.pushDown(rt, mid - l + 1, r - mid)
        ans = 0
        if L <= mid:
            ans += self.query(L, R, l, mid, rt << 1)
        if R > mid:
            ans += self.query(L, R, mid + 1, r, rt << 1 | 1)
        return ans


# 比较器，暴力解法
class Right:
    def __init__(self, origin):
        self.arr = [0] * (len(origin) + 1)
        for i in range(len(origin)):
            self.arr[i + 1] = origin[i]

    def update(self, L, R, C):
        for i in range(L, R + 1):
            self.arr[i] = C

    def add(self, L, R, C):
        for i in range(L, R + 1):
            self.arr[i] += C

    def query(self, L, R):
        ans = 0
        for i in range(L, R + 1):
            ans += self.arr[i]
        return ans


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


def test():
    long = 100
    maxnum = 1000
    testTimes = 5000
    addOrUpdateTimes = 1000
    queryTimes = 500
    for i in range(testTimes):
        origin = generateArray(long, 0, maxnum)
        seg = SegmentTree(origin)
        S, N = 1, len(origin)
        root = 1
        seg.build(S, N, root)
        rig = Right(origin)
        for j in range(addOrUpdateTimes):
            num1 = random.randint(1, N)
            num2 = random.randint(1, N)
            L = min(num1, num2)
            R = max(num1, num2)
            C = random.randint(0, maxnum - 1) - random.randint(0, maxnum - 1)
            if random.random() < 0.5:
                seg.add(L, R, C, S, N, root)
                rig.add(L, R, C)
            else:
                seg.updatefun(L, R, C, S, N, root)
                rig.update(L, R, C)

        for k in range(queryTimes):
            num1 = random.randint(1, N)
            num2 = random.randint(1, N)
            L = min(num1, num2)
            R = max(num1, num2)
            ans1 = seg.query(L, R, S, N, root)
            ans2 = rig.query(L, R)
            if ans2 != ans1:
                print()
                return False
    return True


if __name__ == "__main__":
    origin = [2, 1, 1, 2, 3, 4, 5]
    seg = SegmentTree(origin)
    S = 1  # 整个区间开始的位置，规定从1开始，不从0开始
    N = len(origin)  # 整个区间的结束位置，规定能到N，不是N-1
    root = 1  # 整棵树的头节点
    L = 2  # 操作区间的开始位置
    R = 5  # 操作区间的结束位置
    C = 4  # 要加的数字或者要更新的数字
    seg.build(S, N, root)
    seg.add(L, R, C, S, N, root)
    print(seg.query(L, R, S, N, root))
    seg.updatefun(L, R, C, S, N, root)
    print(seg.query(L, R, S, N, root))
    print("对数器开始……")
    print("测试结果：" + ("通过" if test() else "未通过"))
