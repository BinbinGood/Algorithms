# 给定五个参数n,m,i,j,k。表示在一个N*M的区域，Bob处在(i,j)点，每次Bob等概率的向上、
# 下、左、右四个方向移动一步，Bob必须走K步。如果走完之后，Bob还停留在这个区域上，
# 就算Bob存活，否则就算Bob死亡。请求解Bob的生存概率，返回字符串表示分数的方式。

def process(n, m, i, j, k):
    if i < 0 or j < 0 or i >= n or j >= m or k < 0:
        return 0
    if k == 0:
        return 1
    return process(n, m, i + 1, j, k - 1) \
           + process(n, m, i - 1, j, k - 1) \
           + process(n, m, i, j - 1, k - 1) \
           + process(n, m, i, j + 1, k - 1)


def bobdie1(n, m, i, j, k):
    all = 4 ** k  # 总的可能数
    live = process(n, m, i, j, k)  # 存活的次数
    gcd = maxgcd(all, live)  # 最大公因数
    return f"{live / gcd}/{all / gcd}"


def bobdie2(n, m, i, j, k):
    all = 4 ** k  # 总的可能数
    live = process2(n, m, i, j, k)  # 存活的次数
    gcd = maxgcd(all, live)  # 最大公因数
    return f"{live / gcd}/{all / gcd}"


def process2(n, m, i, j, k):
    if i < 0 or j < 0 or i >= n or j >= m or k < 0:
        return 0
    dp = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    for kindex in range(k + 1):
        for jindex in range(m):
            for iindex in range(n):
                if kindex == 0:
                    dp[iindex][jindex][kindex] = 1
                else:
                    dp[iindex][jindex][kindex] = getvalue(dp, m, n, iindex + 1, jindex, kindex - 1) \
                                                 + getvalue(dp, m, n, iindex - 1, jindex, kindex - 1) \
                                                 + getvalue(dp, m, n, iindex, jindex - 1, kindex - 1) \
                                                 + getvalue(dp, m, n, iindex, jindex + 1, kindex - 1)

    return dp[i][j][k]


def getvalue(dp, m, n, i, j, k):
    if i < 0 or j < 0 or i >= n or j >= m or k < 0:
        return 0
    return dp[i][j][k]


def maxgcd(m, n):
    return m if n == 0 else maxgcd(n, m % n)


if __name__ == "__main__":
    str1 = bobdie1(10, 10, 3, 2, 5)
    str2 = bobdie2(10, 10, 3, 2, 5)
    print(str1)
    print(str2)
