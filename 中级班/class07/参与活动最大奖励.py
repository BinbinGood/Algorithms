# CC直播的运营部门组织了很多运营活动，每个活动需要花费一定的时间参与，主播每参
# 加完一个活动即可得到一定的奖励，参与活动可以从任意活动开始，但一旦开始，就需
# 要将后续活动参加完毕（注意：最后一个活动必须参与），活动之间存在一定的依赖关
# 系（不存在环的情况），现在给出所有的活动时间与依赖关系，以及给出有限的时间，
# 请帮主播计算在有限的时候内，能获得的最大奖励，以及需要的最少时长。
# 如上图数据所示，给定有限时间为10天。可以获取得最大奖励为：11700，需要的时长为：9天。参加的活动为BDFH
# 四个。
# 输入描述：
# 第一行输入数据N与D，表示有N项活动，D表示给予的时长。0＜N＜＝1000，0＜D＜＝10000。
# 从第二行开始到N+1行，每行描述一个活动的信息，其中第一项表示当前活动需要花费的时间t，第二项表示可以获
# 得的奖励a，之后有N项数据，表示当前活动与其他活动的依赖关系，1表示有依赖，0表示无依赖。每项数据用空格
# 分开。
# 输出描述：
# 输出两项数据A与T，用空格分割。A表示所获得的最大奖励，T表示所需要的时长。
# 输入
# 8 10
# 3 2000 0 1 1 0 0 0 0 0
# 3 4000 0 0 0 1 1 0 0 0
# 2 2500 0 0 0 1 0 0 0 0
# 1 1600 0 0 0 0 1 1 1 0
# 4 3800 0 0 0 0 0 0 0 1
# 2 2600 0 0 0 0 0 0 0 1
# 4 4000 0 0 0 0 0 0 0 1
# 3 3500 0 0 0 0 0 0 0 0
# 输出
# 11700

def maxRevenue(alltime, revenue, times, dependents):
    size = len(revenue)
    parent = dict()  # 存放每个节点对应的父节点，父节点通过列表保存
    for i in range(size):
        parent[i] = []
    end = -1  # 用来保存最后一个活动节点
    for i in range(len(dependents)):
        allzero = True  # 若某一行全是0，表示此节点为最后一个活动节点
        for j in range(len(dependents[0])):
            if dependents[i][j] != 0:
                parent[j].append(i)
                allzero = False
        if allzero:
            end = i

    nodeCostRevenueMap = dict()
    for i in range(size):
        nodeCostRevenueMap[i] = dict()
    nodeCostRevenueMap[end][times[end]] = revenue[end]

    queue = [end]
    while queue:
        cur = queue.pop(0)
        for last in parent[cur]:  # 遍历cur的每一个父节点
            for curtime in nodeCostRevenueMap[cur].keys(): # 一定要按顺序遍历和添加
                lastCost = curtime + times[last]
                lastRevenue = nodeCostRevenueMap[cur][curtime] + revenue[last]
                lastmap = nodeCostRevenueMap[last]
                if (MapfloorKey(lastmap, lastCost) is None) or (lastmap[MapfloorKey(lastmap, lastCost)] < lastRevenue):
                    lastmap[lastCost] = lastRevenue
            # print(nodeCostRevenueMap[last])
            queue.append(last)
    # 创建一个最终的表，将所有节点的天数和收益表都汇总到一块
    allmap = dict()
    for curmap in nodeCostRevenueMap.values():
        for curtime in sorted(curmap):  # 一定要按顺序遍历和添加
            Cost = curtime
            Revenue = curmap[curtime]
            if (MapfloorKey(allmap, Cost) is None) or (allmap[MapfloorKey(allmap, Cost)] < Revenue):
                allmap[Cost] = Revenue
    print(allmap)
    return [MapfloorKey(allmap, alltime), allmap[MapfloorKey(allmap, alltime)]]
    # return 0


def MapfloorKey(hashmap, key):
    while key >= 0:
        if key in hashmap:
            return key
        key -= 1
    return None


allTime = 10
revenue = [2000, 4000, 2500, 1600, 3800, 2600, 4000, 3500]
times = [3, 3, 2, 1, 4, 2, 4, 3]
dependents = [[0, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0]]
res = maxRevenue(allTime, revenue, times, dependents)
print(res)
