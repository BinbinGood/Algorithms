# 【题目】
# 假设有排成一行的 N 个位置，记为 1~N，N 一定大于或等于 2。开始时机器人在其中的 M 位
# 置上(M 一定是 1~N 中的一个)，机器人可以往左走或者往右走，如果机器人来到 1 位置， 那
# 么下一步只能往右来到 2 位置;如果机器人来到 N 位置，那么下一步只能往左来到 N-1 位置。
# 规定机器人必须走 K 步，最终能来到 P 位置(P 也一定是 1~N 中的一个)的方法有多少种。给
# 定四个参数 N、M、K、P，返回方法数。
def RobotWalk1(N, M, K, P):
    return process1(N, M, K, P)


# 暴力递归
def process1(N, cur, rest, P):
    if rest == 0:
        return 1 if cur == P else 0
    if cur == 1:
        return process1(N, 2, rest - 1, P)
    if cur == N:
        return process1(N, N - 1, rest - 1, P)
    return process1(N, cur - 1, rest - 1, P) + process1(N, cur + 1, rest - 1, P)


# 记忆搜索(DP)
def RobotWalk2(N, M, K, P):
    dp = [[-1] * (K + 1) for _ in range(N + 1)]
    return process2(N, M, K, P, dp)


def process2(N, cur, rest, P, dp):
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:
        dp[cur][rest] = 1 if cur == P else 0
    elif cur == 1:
        dp[cur][rest] = process2(N, 2, rest - 1, P, dp)
    elif cur == N:
        dp[cur][rest] = process2(N, N - 1, rest - 1, P, dp)
    else:
        dp[cur][rest] = process2(N, cur - 1, rest - 1, P, dp) + process2(N, cur + 1, rest - 1, P, dp)
    return dp[cur][rest]


# 严格表结构(DP)
def RobotWalk3(N, M, K, P):
    if N < 2 or M < 1 or K < 1 or M > N or P < 1 or P > N:
        return 0
    dp = [[-1] * (K + 1) for _ in range(N + 1)]
    for rest in range(0, K + 1, 1):
        for cur in range(1, N + 1, 1):
            if rest == 0:
                dp[cur][rest] = 1 if cur == P else 0
            elif cur == 1:
                dp[cur][rest] = dp[2][rest - 1]
            elif cur == N:
                dp[cur][rest] = dp[N - 1][rest - 1]
            else:
                dp[cur][rest] = dp[cur - 1][rest - 1] + dp[cur + 1][rest - 1]
    return dp[M][K]


if __name__ == "__main__":
    print(RobotWalk1(3, 1, 3, 3))
    print(RobotWalk2(3, 1, 3, 3))
    print(RobotWalk3(5, 2, 3, 3))
