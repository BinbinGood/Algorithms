# N个加油站组成一个环形，给定两个长度都是N的非负数组 oil和dis(N>1)，oil[i]代表
# 第i个加油站存的油可以跑多少千米，dis[i]代表第i个加油站到环中下一个加油站相隔
# 多少千米。
# 假设你有一辆油箱足够大的车，初始时车里没有油。如果车从第i个加油站出发，最终
# 可以回到这个加油站，那么第i个加油站就算良好出发点，否则就不算。
# 请返回长度为N的boolean型数组res，res[i]代表第 i 个加油站是不是良好出发点。

def stations(oil, dis):
    if (len(oil) < 2) or (len(oil) != len(dis)):
        return None
    init = -1
    for i in range(len(oil)):
        dis[i] = oil[i] - dis[i]
        if dis[i] >= 0:
            init = i
    return [False] * len(oil) if init == -1 else enlargeArea(dis, init)


def enlargeArea(dis, init):
    res = [False] * len(dis)
    start = init
    end = nextindex(init, len(dis))
    rest = 0
    need = 0

    # 没有do-while只能这么写了
    if dis[start] < need:
        need -= dis[start]
    else:
        rest += dis[start] - need
        need = 0
        while rest >= 0 and end != start:
            rest += dis[end]
            end = nextindex(end, len(dis))
        if rest >= 0:
            res[start] = True
            connectGood(dis, lastindex(start, len(dis)), init, res)
            return res
    start = lastindex(start, len(dis))
    while start != init:
        # 当前来到的start已经在连通区域中，可以确定后续的开始点一定无法转完一圈
        if (start != init) and (start == lastindex(end, len(dis))):
            break
        # 当前来到的start不在连通区域中，就扩充连通区域
        if dis[start] < need:
            need -= dis[start]
        else:  # 如start可以到达initial点，扩充连通区域的结束点
            rest += dis[start] - need
            need = 0
            while (rest >= 0) and (end != start):  # 连通区尾巴逆时针扩，这里左右两个边界都算上了
                rest += dis[end]
                end = nextindex(end, len(dis))
            # 循环结束时有两种情况，rest < 0或者走完一圈
            # （走完一圈了）如果连通区域已经覆盖整个环，当前的start是良好出发点，进入2阶段
            if rest >= 0:
                res[start] = True
                connectGood(dis, lastindex(start, len(dis)), init, res)
                break
        start = lastindex(start, len(dis))
    return res


# 已知start的next方向上有一个良好出发点
# start如果可以达到这个良好出发点，那么从start出发一定可以转一圈
# init为初始出发点，res存放结果，dis表示纯能值数组
def connectGood(dis, start, init, res):
    need = 0
    while start != init:
        if dis[start] < need:
            need -= dis[start]
        else:
            res[start] = True
            need = 0
        start = lastindex(start, len(dis))


def nextindex(index, size):
    return 0 if index == size - 1 else index + 1


def lastindex(index, size):
    return size - 1 if index == 0 else index - 1


oil = [4, 5, 3, 1, 5, 1, 1, 9]
dis = [1, 9, 1, 2, 6, 0, 2, 0]
print(stations(oil, dis))
