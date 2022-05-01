# 给定一个二维数组matrix，每个单元都是一个整数，有正有负。最开始的时候小Q操纵
# 一条长度为0的蛇蛇从矩阵最左侧任选一个单元格进入地图，蛇每次只能够到达当前位
# 置的右上相邻，右侧相邻和右下相邻的单元格。蛇蛇到达一个单元格后，自身的长度会
# 瞬间加上该单元格的数值，任何情况下长度为负则游戏结束。小Q是个天才，他拥有一
# 个超能力，可以在游戏开始的时候把地图中的某一个节点的值变为其相反数（注：最多
# 只能改变一个节点）。问在小Q游戏过程中，他的蛇蛇最长长度可以到多少？
# 比如：
# 1 -4 10
# 3 -2 -1
# 2 -1 0
# 0 5 -2
# 最优路径为从最左侧的3开始，3 -> -4(利用能力变成4) -> 10。所以返回17。

def snakeMaxlong(matrix):
    res = matrix[0][0]
    if len(matrix) == 0:
        return 0
    dp = [[[0] * 2 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):  # 最左列
        dp[i][0][0] = matrix[i][0]  # 不使用
        dp[i][0][1] = -matrix[i][0]  # 使用超能力
        res = max(res, max(dp[i][0][0], dp[i][0][1]))  # 更新最大值
    for j in range(1, len(matrix[0])):  # 列
        for i in range(len(matrix)):  # 行
            preno = -1  # 之前不用超能力取得的最大值
            preyes = -1  # 之前使用过超能力取得的最大值
            if i > 0:
                if dp[i - 1][j - 1][0] >= 0:
                    preno = max(preno, dp[i - 1][j - 1][0])
                if dp[i - 1][j - 1][1] >= 0:
                    preyes = max(preyes, dp[i - 1][j - 1][1])
            if dp[i][j - 1][0] >= 0:
                preno = max(preno, dp[i][j - 1][0])
            if dp[i][j - 1][1] >= 0:
                preyes = max(preyes, dp[i][j - 1][1])
            if i < len(matrix) - 1:
                if dp[i + 1][j - 1][0] >= 0:
                    preno = max(preno, dp[i + 1][j - 1][0])
                if dp[i + 1][j - 1][1] >= 0:
                    preyes = max(preyes, dp[i + 1][j - 1][1])
            no = -1  # 一次能力也不用，能达到的最大路径和。（如果是负数，表示没有该答案）
            yes = -1  # 使用了一次能力，能达到的最大路劲和。（如果是负数，表示没有该答案）
            if preno >= 0:
                no = preno + matrix[i][j]
                yes = preno - matrix[i][j]
            if preyes >= 0:
                yes = max(preyes + matrix[i][j], yes)
            dp[i][j][0] = no
            dp[i][j][1] = yes
            res = max(res, max(dp[i][j][0], dp[i][j][1]))  # 更新最大值
    return res


matrix1 = [[1, -4, 10],
           [3, -2, -1],
           [2, -1, 0],
           [0, 5, -2]]
print(snakeMaxlong(matrix1))
