# 请同学们自行搜索或者想象一个象棋的棋盘，然后把整个棋盘放入第一象限，棋盘的最左下
# 角是(0,0)位置。那么整个棋盘就是横坐标上9条线、纵坐标上10条线的一个区域。给你三个
# 参数，x，y，k，返回如果“马”从(0,0)位置出发，必须走k步，最后落在(x,y)上的方法数
# 有多少种？

def process(x, y, step):
    if x < 0 or x > 8 or y < 0 or y > 9:
        return 0
    if step == 0:
        return 1 if (x == 0 and y == 0) else 0
    return process(x - 1, y + 2, step - 1) + process(x - 1, y - 2, step - 1) \
           + process(x + 1, y + 2, step - 1) + process(x + 1, y - 2, step - 1) \
           + process(x - 2, y + 1, step - 1) + process(x - 2, y - 1, step - 1) \
           + process(x + 2, y + 1, step - 1) + process(x + 2, y - 1, step - 1)


def getways1(x, y, k):
    if k < 0:
        return 0
    return process(x, y, k)


def getways2(x, y, k):
    if k < 0 or x < 0 or x > 8 or y < 0 or y > 9:
        return 0
    dp = [[[0] * (k + 1) for _ in range(10)] for _ in range(9)]  # [9][10][k+1]
    for step in range(k + 1):
        if step == 0:
            dp[0][0][step] = 1
            continue
        for xindex in range(9):
            for yindex in range(10):
                dp[xindex][yindex][step] = getvalue(dp, xindex - 1, yindex + 2, step - 1) \
                                           + getvalue(dp, xindex + 1, yindex + 2, step - 1) \
                                           + getvalue(dp, xindex - 1, yindex - 2, step - 1) \
                                           + getvalue(dp, xindex + 1, yindex - 2, step - 1) \
                                           + getvalue(dp, xindex - 2, yindex + 1, step - 1) \
                                           + getvalue(dp, xindex - 2, yindex - 1, step - 1) \
                                           + getvalue(dp, xindex + 2, yindex + 1, step - 1) \
                                           + getvalue(dp, xindex + 2, yindex - 1, step - 1)
    return dp[x][y][k]


# 因为索引可能越界，所以需要此函数判断是否越界，越界就返回0
def getvalue(dp, x, y, k):
    if k < 0 or x < 0 or x > 8 or y < 0 or y > 9:
        return 0
    return dp[x][y][k]


if __name__ == "__main__":
    print(getways1(7, 7, 10))
    print(getways2(7, 7, 10))
