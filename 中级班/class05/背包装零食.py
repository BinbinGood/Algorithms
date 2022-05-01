# 牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容
# 量为w。
# 牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
# 牛牛想知道在总体积不超过背包容量的情况下，他一共有多少种零食放法(总体积为0也
# 算一种放法)。

def getways1(v, w):
    return process(v, 0, w)


def process(v, i, rest):
    if rest < 0:
        return 0
    if i == len(v):
        return 1
    return process(v, i + 1, rest - v[i]) + process(v, i + 1, rest)


def getways2(v, w):
    dp = [[0] * (w + 1) for _ in range(len(v) + 1)]
    for rest in range(len(dp[0])):
        dp[len(v)][rest] = 1
    for i in range(len(dp) - 2, -1, -1):
        for rest in range(len(dp[0])):
            dp[i][rest] = getvalue(dp, i + 1, rest - v[i]) + getvalue(dp, i + 1, rest)
    return dp[0][w]


def getvalue(dp, i, rest):
    if rest < 0:
        return 0
    return dp[i][rest]


if __name__ == "__main__":
    v = [1, 5, 1, 8, 3, 7, 2]
    print(getways1(v, 6))
    print(getways2(v, 6))
