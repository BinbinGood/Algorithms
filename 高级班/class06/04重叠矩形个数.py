# 平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i],
# y2[i])。如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角
# 落)。请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。
from sortedcontainers import SortedSet


class rectangle:
    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right


# 输入一系列矩形
def maxCover(rescs):
    if (rescs is None) or (len(rescs) == 0):
        return 0
    rescs.sort(key=lambda x: x.down)
    leftOrder = SortedSet(key=lambda x: x.left)
    res = 0
    i = 0
    while i < len(rescs):
        curdown = rescs[i].down
        index = i
        # 将矩阵下边相同的矩形全部加入有序表中
        while (index < len(rescs)) and (rescs[index].down == curdown):
            leftOrder.add(rescs[index])
            index += 1
        i = index
        removeLowerOnCurDown(leftOrder, curdown)
        # 最多重叠线段的计算方法 O(Nlog(N))
        rightOrder = SortedSet(key=lambda x: x.right)
        for rec in leftOrder:
            removeLeftOnCurLeft(rightOrder, rec.left)
            rightOrder.add(rec)
            res = max(res, len(rightOrder))
        # i += 1
    return res


# 把leftset中上边小于等于curdown的矩阵全部删除
def removeLowerOnCurDown(leftset, curdown):
    removes = []
    for rec in leftset:
        if rec.up <= curdown:
            removes.append(rec)
    for rec in removes:
        leftset.remove(rec)


# 把rightset有序表中，右边结尾小于等于curleft的矩形全部删除
def removeLeftOnCurLeft(rightset, curleft):
    removes = []
    for rec in rightset:
        if rec.right > curleft:
            break
        removes.append(rec)
    for rec in removes:
        rightset.remove(rec)


recs = [rectangle(2, 1, 3, 4),rectangle(4,1,2,4),rectangle(3,2,1,3),rectangle(3,1,0,3)]
print(maxCover(recs))
