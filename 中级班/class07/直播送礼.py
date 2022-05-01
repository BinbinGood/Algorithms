# CC里面有一个土豪很喜欢一位女直播Kiki唱歌，平时就经常给她点赞、送礼、私聊。最近CC直播平台在举行
# 中秋之星主播唱歌比赛，假设一开始该女主播的初始人气值为start， 能够晋升下一轮人气需要刚好达到end，
# 土豪给主播增加人气的可以采取的方法有：
# a. 点赞 花费x C币，人气 + 2
# b. 送礼 花费y C币，人气 * 2
# c. 私聊 花费z C币，人气 - 2
# 其中 end 远大于start且end为偶数， 请写一个程序帮助土豪计算一下，最少花费多少C币就能帮助该主播
# Kiki将人气刚好达到end，从而能够晋级下一轮？
# 输入描述：
# 第一行输入5个数据，分别为：x y z start end，每项数据以空格分开。
# 其中：0＜x, y, z＜＝10000， 0＜start, end＜＝1000000
# 输出描述：
# 需要花费的最少C币。
# 示例1:
# 输入
# 3 100 1 2 6
# 输出
# 6

def Minconins(x, y, z, start, end):
    if x < 0 or x > 10000 or y < 0 or y > 10000 or z < 0 or z > 10000 or start < 0 or end > 1000000 or end < 0 or end > 1000000:
        return -1
    if start > end:
        return -1
    return process(x, y, z, start, end)


# 观察下面的这个递归，可以发现这个递归永远无法跑完，会陷入死循环.缺少basecase
# cur表示当前已经来到的人气值
# end是目标人气值
def process(x, y, z, cur, end):
    if cur == end:
        return 0
    way1 = process(x, y, z, cur + 2, end) + x  # 方法一
    way2 = process(x, y, z, cur * 2, end) + y  # 方法二
    way3 = process(x, y, z, cur - 2, end) + z  # 方法三
    return min(way3, min(way2, way1))


def Minconins1(x, y, z, start, end):
    if x < 0 or x > 10000 or y < 0 or y > 10000 or z < 0 or z > 10000 or start < 0 or end > 1000000 or end < 0 or end > 1000000:
        return -1
    if start > end:
        return -1
    limitcons = (end - start) * x // 2  # 优化一，通用方法。找到一个平凡解，一直通过点赞的方式一定可以到达目标人气
    limitend = 2 * end  # 优化二，不具有通用性。无论哪一种方式，最高的人气值一定不会到达目标人气的二倍
    return process1(0, x, y, z, start, end, limitend, limitcons)


# cur 表示当前的人气，end表示目标人气
# pre 表示当前已经花费的钱数
def process1(pre, x, y, z, cur, end, limitend, limitcons):
    if cur > limitend:
        return limitcons  # 因为python没有系统最大值，用这个代替
    if pre > limitcons:
        return limitcons
    if cur < 0:
        return limitcons
    if cur == end:
        return pre
    mincons = limitcons
    p1 = process1(pre + x, x, y, z, cur + 2, end, limitend, limitcons)
    if p1 != limitcons:
        mincons = p1
    p2 = process1(pre + y, x, y, z, cur * 2, end, limitend, limitcons)
    if p2 != limitcons:
        mincons = min(mincons, p2)
    p3 = process1(pre + z, x, y, z, cur - 2, end, limitend, limitcons)
    if p3 != limitcons:
        mincons = min(mincons, p3)
    return mincons


# 暴力递归改动态规划
def Minconins2(x, y, z, start, end):
    if x < 0 or x > 10000 or y < 0 or y > 10000 or z < 0 or z > 10000 or start < 0 or end > 1000000 or end < 0 or end > 1000000:
        return -1
    if start > end:
        return -1
    limitcons = (end - start) * x // 2  # 优化一，通用方法。找到一个平凡解，一直通过点赞的方式一定可以到达目标人气
    limitend = 2 * end  # 优化二，不具有通用性。无论哪一种方式，最高的人气值一定不会到达目标人气的二倍
    dp = [[limitcons] * (limitend + 1) for _ in range(limitcons + 1)]
    for pre in range(len(dp) - 1, -1, -1):
        for cur in range(len(dp[0])):
            if cur == end:
                dp[pre][cur] = pre
            else:
                if pre + x <= limitcons and cur + 2 <= limitend:  # 保证不越界
                    dp[pre][cur] = min(dp[pre + x][cur + 2], dp[pre][cur])
                if pre + z <= limitcons and cur - 2 >= 0:
                    dp[pre][cur] = min(dp[pre + z][cur - 2], dp[pre][cur])
                if pre + y <= limitcons and cur * 2 <= limitend:
                    dp[pre][cur] = min(dp[pre + y][cur * 2], dp[pre][cur])
    return dp[0][start]


x, y, z, start, end = 3, 5, 1, 10, 30
print(Minconins1(x, y, z, start, end))  # 此时的最优方案为：z,y,y,z
print(Minconins2(x, y, z, start, end))
