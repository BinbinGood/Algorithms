# 请注意区分子串和子序列的不同，给定两个字符串str1和str2，求两个字符串
# 的最长公共子序列
# 动态规划空间压缩的技巧讲解

def Maxlongstr(str1, str2):
    dp = [[0] * len(str2) for _ in range(len(str1))]
    # 填表的边界
    for j in range(len(str2)):
        dp[0][j] = dp[0][j - 1]
        if str1[0] == str2[j]:
            dp[0][j] += 1
    for i in range(1, len(str1)):
        dp[i][0] = dp[i - 1][0]
        if str1[i] == str2[0]:
            dp[i][0] += 1
    # 填一般位置
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = dp[i - 1][j - 1]  # 情况一，不以ij结尾
            if str1[i] == str2[j]:  # 情况四，如果当前位置字符相等，还要+1
                dp[i][j] += 1
            dp[i][j] = max(dp[i][j], max(dp[i - 1][j], dp[i][j - 1]))  # 情况二、三，分别不以i或者j结尾
    return dp[len(str1) - 1][len(str2) - 1]


str1 = "A1BC2D3EFGH45I6JK7LMN"
str2 = "12OPQ3RST4U5V6W7XYZ"
print(Maxlongstr(str1, str2))
