# 给定一个字符串str，求最长的回文子序列。注意区分子序列和子串的不同。
# 字符列可以不重复
def Maxlonghuistr(str1):
    if len(str1) == 0:
        return 0
    dp = [[0] * len(str1) for _ in range(len(str1))]
    for k in range(len(str1)):  # 对角线都为1
        dp[k][k] = 1
    i, j = 0, 1
    while i < len(str1) - 1:
        dp[i][j] = 2 if str1[i] == str1[j] else 1
        i += 1
        j += 1
    for i in range(len(str1) - 3, -1, -1):
        for j in range(i + 2, len(str1)):
            dp[i][j] = dp[i + 1][j - 1]
            if str1[i] == str1[j]:
                dp[i][j] += 2
            dp[i][j] = max(dp[i][j], max(dp[i + 1][j], dp[i][j - 1]))
    return dp[0][len(str1) - 1]


str1 ="A1BC2D33FG2H1I"
print(Maxlonghuistr(str1))
