# 给定一个 N×3 的矩阵 matrix，对于每一个长度为 3 的小数组 arr，都表示一个大楼的三个数
# 据。arr[0]表示大楼的左边界，arr[1]表示大楼的右边界，arr[2]表示大楼的高度(一定大于 0)。
# 每座大楼的地基都在 X 轴上，大楼之间可能会有重叠，请返回整体的轮廓线数组。
# 【举例】
# matrix = {
# {2,5,6},
# {1,7,4},
# {4,6,7},
# {3,6,5},
# {10,13,2},
# {9,11,3},
# {12,14,4},
# {10,12,5}
# }
# 返回：
# {{1,2,4},
# {2,4,6},
# {4,6,7},
# {6,7,4},
# {9,10,3},
# {10,12,5},
# {12,14,4}}

from sortedcontainers import SortedDict


def buildingOutline(matrix):
    nodes = []
    for i in range(len(matrix)):
        # 每个大楼都会产生两个数据，起点处增加，终点处删除
        nodes.append([matrix[i][0], 0, matrix[i][2]])  # 0表示高度增加，1表示高度删除
        nodes.append([matrix[i][1], 1, matrix[i][2]])
    nodes.sort(key=lambda x: (x[0], x[1]))

    mapheightTimes = SortedDict()  # 楼高和出现的次数
    mapvalueHeight = SortedDict()  # 当前位置，楼的最大高度
    for i in range(len(nodes)):
        if nodes[i][1] == 0:  # 当前是增加操作
            if nodes[i][2] not in mapheightTimes:
                mapheightTimes[nodes[i][2]] = 1
            else:
                mapheightTimes[nodes[i][2]] += 1
        else:  # 删除操作
            if mapheightTimes[nodes[i][2]] == 1:
                del mapheightTimes[nodes[i][2]]
            else:
                mapheightTimes[nodes[i][2]] -= 1

        if len(mapheightTimes) == 0:
            mapvalueHeight[nodes[i][0]] = 0
        else:
            mapvalueHeight[nodes[i][0]] = mapheightTimes.peekitem()[0]

    res = []
    stat = mapvalueHeight.peekitem(0)[0]
    preheight = mapvalueHeight.peekitem(0)[1]
    for k, v in mapvalueHeight.items():
        curx = k
        curmaxheight = v
        if preheight != curmaxheight:
            res.append([stat, preheight])
            stat = curx
            preheight = curmaxheight
    res.append([mapvalueHeight.peekitem()[0],mapvalueHeight.peekitem()[1]])
    return res


# matrix1 = [[2, 5, 6],
#             [1, 7, 4],
#             [4, 6, 7],
#             [3, 6, 5],
#             [10, 13, 2],
#             [9, 11, 3],
#             [12, 14, 4],
#             [10, 12, 5]]
print(buildingOutline([[0,2,3],[2,5,3]]))
