# 给值加上一层，叫元素
# 此操作可以防止后续用户给你相同的值出现混乱
class element():
    def __init__(self, value):
        self.value = value


class UnionFindSet():
    def __init__(self, list):
        # 保存值和对应的元素
        self.elementMap = {}
        # 保存元素和其对应的父节点元素
        self.fatherMap = {}
        # 保存代表元素和它的子节点的数量
        self.sizeMap = {}
        for value in list:
            ele = element(value)
            self.elementMap[value] = ele
            # 每个元素的父节点初始化都指向自身
            self.fatherMap[ele] = ele
            # 为每个元素都创建为代表元素
            self.sizeMap[ele] = 1

    # 该函数给定元素寻找其代表元素，沿着他的父节点一直向上找，直到元素的父节点为其本身，表示找到代表元素
    # 同时利用栈保存寻找代表元素的路径，将这些路径点的父节点都修改为代表元素，（扁平化）
    def findHead(self, element):
        stack = []
        while self.fatherMap[element] != element:
            stack.append(element)
            element = self.fatherMap[element]

        while stack:
            self.fatherMap[stack.pop()] = element
        return element

    # 判断两个值是否属于同一集合
    def isSameSet(self, a, b):
        if (a in self.elementMap) and (b in self.elementMap):
            return self.findHead(self.elementMap[a]) == self.findHead(self.elementMap[b])
        return False

    # 将两个值所在的集合合并在一起
    def UnionSets(self, a, b):
        if (a in self.elementMap) and (b in self.elementMap):
            af = self.findHead(self.elementMap[a])
            bf = self.findHead(self.elementMap[b])
            if af != bf:
                big = bf  # 找到两个代表元素中包含元素多的那一个作为合并以后的代表元素
                small = af
                if self.sizeMap[af] > self.sizeMap[bf]:
                    big = af
                    small = bf
                self.fatherMap[small] = big  # 将小的集合的代表元素的父节点指向大的集合的代表元素
                self.sizeMap[big] = self.sizeMap[big] + self.sizeMap[small]  # 修改大集合的代表元素包含的元素个数
                del self.sizeMap[small]  # 删除小集合代表元素


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6]
    unionfind = UnionFindSet(list1)
    print(unionfind.isSameSet(1, 2))
    unionfind.UnionSets(1, 2)
    print(unionfind.isSameSet(1, 2))
