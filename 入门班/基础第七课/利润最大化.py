# 输入：
# 正数数组costs
# 正数数组profits
# 正数k
# 正数m
# 含义：
# costs[i]表示i号项目的花费
# profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
# k表示你只能串行的最多做k个项目
# m表示你初始的资金
# 说明：
# 你每做完一个项目，马上获得的收益，可以支持你去做下一个项目。
# 输出：
# 你最后获得的最大钱数。
import heapq


def findMaximizedCapital(costs, profits, k, m):
    nodes = []
    for i in range(len(profits)):
        nodes.append([profits[i], costs[i]])
    nodes.sort(key=lambda x: x[1])  # 按照项目费用排序
    i = 0
    cur = 0
    maxprofitheap = []
    while i < k:
        while cur < len(nodes) and nodes[cur][1] <= m:
            heapq.heappush(maxprofitheap, -nodes[cur][0])
            cur += 1
        if maxprofitheap:
            m -= heapq.heappop(maxprofitheap)
        else:
            break
        i += 1
    return m


if __name__ == "__main__":
    costs = [1, 1, 2]
    profits = [1, 2, 3]
    print(findMaximizedCapital(costs, profits, 3, 3))
