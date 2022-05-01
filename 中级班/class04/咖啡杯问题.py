# 题目描述
# 首先，给你几个数据：
# 数组arr：表示几个咖啡机，这几个咖啡机生产一杯咖啡所需要的时间就是数组中的值，
#   例如arr=[2,3,7]就表示第一台咖啡机生产一杯咖啡需要2单位时间，第二台需要3单位时间，第三台需要7单位时间。
# int N：表示有N个人需要用咖啡机制作咖啡，每人一杯，同时，假设制作完咖啡后，喝咖啡时间为0，一口闷。
# int a：表示用洗碗机洗一个咖啡杯需要的时间，串行运行。
# int b：表示咖啡杯也可以不洗，自然晾干的时间，咖啡杯要么洗，要么晾干。
# 现在，请你求出这N个人从开始用咖啡杯制作咖啡到杯子洗好或者晾干的最少时间？
import heapq


def getcoffee1(arr, n, a, b):
    if len(arr) == 0 or n <= 0:
        return
    smallheap = []  # 小根堆中存放的是当前是个数组[选择当前咖啡机获得咖啡的时间点,咖啡机制作一杯咖啡的时间]
    for i in range(len(arr)):
        heapq.heappush(smallheap, [arr[i], arr[i]])
    getcoffeetime = []
    for i in range(n):
        cur = heapq.heappop(smallheap)
        getcoffeetime.append(cur[0])
        heapq.heappush(smallheap, [cur[0] + cur[1], cur[1]])
    return process1(getcoffeetime, a, b, 0, 0)


# 暴力递归求洗杯子结束的时间
def process1(getcoffeetim, a, b, i, waterline):
    if i == len(getcoffeetim):
        return waterline
    water = max(getcoffeetim[i], waterline) + a  # 选择用洗咖啡机洗杯子，结束的时间
    next1 = process1(getcoffeetim, a, b, i + 1, water)
    p1 = max(water, next1)

    dry = getcoffeetim[i] + b  # 选择自然风干
    next2 = process1(getcoffeetim, a, b, i + 1, waterline)
    p2 = max(dry, next2)

    return min(p1, p2)


def getcoffee2(arr, n, a, b):
    if len(arr) == 0 or n <= 0:
        return
    smallheap = []  # 小根堆中存放的是当前是个数组[选择当前咖啡机获得咖啡的时间点,咖啡机制作一杯咖啡的时间]
    for i in range(len(arr)):
        heapq.heappush(smallheap, [arr[i], arr[i]])
    getcoffeetime = []
    for i in range(n):
        cur = heapq.heappop(smallheap)
        getcoffeetime.append(cur[0])
        heapq.heappush(smallheap, [cur[0] + cur[1], cur[1]])

    dp = [[0] * (getcoffeetime[n - 1] + n * a) for _ in range(n)]  # 准备一张足够大的表
    for time in range(len(dp[0])):
        dp[n - 1][time] = min(max(getcoffeetime[n - 1], time) + a, getcoffeetime[n - 1] + b)
    for i in range(n - 2, -1, -1):
        waterline = getcoffeetime[i] + (i + 1) * a
        for time in range(waterline):
            water = max(getcoffeetime[i], time) + a  # 选择用洗咖啡机洗杯子，结束的时间
            next1 = dp[i + 1][water]
            dry = getcoffeetime[i] + b  # 选择自然风干
            next2 = dp[i + 1][time]
            dp[i][time] = min(max(water, next1), max(dry, next2))
    return dp[0][0]


if __name__ == "__main__":
    arr = [2, 3, 7]
    N = 10
    a, b = 1, 3
    print(getcoffee1(arr, N, a, b))
    print(getcoffee2(arr, N, a, b))
