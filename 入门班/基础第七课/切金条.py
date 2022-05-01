# 一块金条切成两半，是需要花费和长度数值一样的铜板的。比如长度为20的金条，不管切成长度多大的两半，都要花费20个铜板。
# 一群人想整分整块金条，怎么分最省铜板?
# 例如,给定数组{10,20,30}，代表一共三个人，整块金条长度为10+20+30=60。
# 金条要分成10,20,30三个部分。 如果先把长度60的金条分成10和50，花费60；
# 再把长度50的金条分成20和30，花费50；一共花费110铜板。
# 但是如果先把长度60的金条分成30和30，花费60；再把长度30金条分成10和20，
# 花费30；一共花费90铜板。
# 输入一个数组，返回分割的最小代价
import heapq


# 使用哈夫曼树
def LessMoneySplitGold(str1):
    heapq.heapify(str1)
    sum = 0
    while len(str1) > 1:
        cur = heapq.heappop(str1)
        cur += heapq.heappop(str1)
        sum += cur
        heapq.heappush(str1, cur)
    return sum


if __name__ == "__main__":
    str = [6, 7, 8, 9]
    print(LessMoneySplitGold(str))
