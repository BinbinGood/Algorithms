# 给定一个正数1，裂开的方法有一种，(1)
# 给定一个正数2，裂开的方法有两种，(1和1)、(2)
# 给定一个正数3，裂开的方法有三种，(1、1、1)、(1、2)、(3)
# 给定一个正数4，裂开的方法有五种，(1、1、1、1)、(1、1、2)、(1、3)、（2、2）、
# （4）
# 给定一个正数n，求裂开的方法数。
# 动态规划优化状态依赖的技巧
def getWays(n):
    if n < 1:
        return
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for pre in range(1, n + 1):
        dp[pre][0] = 1
    for k in range(n + 1):
        dp[k][k] = 1
    for pre in range(n - 1, 0, -1):  # 舍弃第0行
        for rest in range(pre + 1, n + 1, 1):
            dp[pre][rest] = dp[pre + 1][rest] + dp[pre][rest - pre]  # 用到了斜率优化
            # if rest - pre >= 0:
            #     dp[pre][rest] += dp[pre][rest - pre]
    return dp[1][n]


for i in range(1,50):
    print(f'{i}输出：{getWays(i)}')
