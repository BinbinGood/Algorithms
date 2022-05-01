# 现有n1+n2种面值的硬币，其中前n1种为普通币，可以取任意枚，后n2种为纪念币，
# 每种最多只能取一枚，每种硬币有一个面值，问能用多少种方法拼出m的面值？


# 可以选任意张
def getn1ways(n1, m):
    # dp表示用i到len(n1)-1之间的面额，拼出指定的钱数
    dp = [[0] * (m + 1) for _ in range(len(n1) + 1)]
    dp[len(n1)][0] = 1
    for i in range(len(n1) - 1, -1, -1):
        for money in range(len(dp[0])):
            dp[i][money] = dp[i + 1][money]
            if money - n1[i] >= 0:  # 优化版本
                dp[i][money] += dp[i][money - n1[i]]
            # ways = 0  # 原始版本
            # zhang = 0
            # while (zhang * n1[i]) <= money:
            #     ways += dp[i + 1][money - zhang * n1[i]]
            #     zhang += 1
            # dp[i][money] = ways
    return dp


# 每种面额最多只能选一张
def getn2ways(n2, m):
    dp = [[0] * (m + 1) for _ in range(len(n2) + 1)]
    dp[len(n2)][0] = 1
    for i in range(len(n2) - 1, -1, -1):
        for money in range(len(dp[0])):
            dp[i][money] = dp[i + 1][money]
            if money - n2[i] >= 0:  # 每种面额只能选一张
                dp[i][money] += dp[i + 1][money - n2[i]]
    return dp


def getn1n2ways(n1, n2, m):
    if m < 0:
        return 0
    dp1 = getn1ways(n1, m)
    dp2 = getn2ways(n2, m)
    res = 0
    for i in range(m):
        res += dp1[0][i] + dp2[0][m - i]
    return res


str1 = [3, 5, 20, 100, 50, 5, 7, 2, 1, 9, 10, 70]
str2 = [6, 8, 4, 2, 9, 10, 5, 1, 25]
print(getn1n2ways(str1, str2, 50))
