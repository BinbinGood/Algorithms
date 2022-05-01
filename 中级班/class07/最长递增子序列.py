# 求最长递增子序列，子序列可以不连续。


# dp[i]表示子序列以arr[i]结尾的情况下的最长子序列长度
# 其中，对于第i个位置的值arr[i]向左边遍历比arr[i]小的数，取其中子序列最大的作为arr[i]的倒数第二个元素。这样：dp[i]=子序列最大的+1
import random


def Maxstrway1(arr):
    if len(arr) == 0:
        return 0
    dp = [1] * len(arr)
    res = 0
    for i in range(len(arr)):  # 此方法为O（N方）
        tempmin = 0
        for j in range(0, i):
            if arr[j] < arr[i]:  # 如果左边遇到了比arr[i]小的数，就更新最长子序列的长度
                tempmin = max(tempmin, dp[j])
        dp[i] = tempmin + 1  # 最后将得到的左边最长子序列长度+1
        res = max(res, dp[i])
    return res


# 更进一步要求打印最长子序列
def Maxstrway2(arr):
    if len(arr) == 0:
        return 0
    dp = [1] * len(arr)
    pre = [i for i in range(len(arr))]  # 前驱元素数组，记录当前以该元素结尾的递增序列中该元素的前驱节点，用于打印序列使用
    res = 1  # 记录最长自序列的长度
    k = 0
    for i in range(len(arr)):  # 此方法为O（N方）
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:  # 如果左边遇到了比arr[i]小的数,同时要保证新添加的这个数所形成的序列会更长，就更新最长子序列的长度
                dp[i] = dp[j] + 1
                pre[i] = j
                if res < dp[i]:  # 记录最大长度和对应的结尾位置
                    res = dp[i]
                    k = i
    # 输出该序列
    i = res - 1
    result = [0] * res  # 存放结果
    while pre[k] != k:  # 利用前驱数组一直往前跳，直到走到前驱数组只想自己的元素，表示此位置是最后一个，结束循环
        result[i] = arr[k]
        i -= 1
        k = pre[k]  # 往前跳
    result[i] = arr[k]  # 将最后一个元素加入返回数组中
    return res


# ends[i]表示所有长度为i+1的递增子序列最小结尾,此方法的时间复杂度为O(NlgN)
def Maxstrway3(arr):
    ends = [0] * len(arr)
    size = 0
    # pre = [i for i in range(len(arr))]  # 前驱元素数组，记录当前以该元素结尾的递增序列中该元素的前驱节点，用于打印序列使用
    # k = 0
    for i in range(len(arr)):
        lo, hi = 0, size
        while lo != hi:
            mid = lo + (hi - lo) // 2
            if ends[mid] < arr[i]:
                lo = mid + 1
            else:
                hi = mid
        ends[lo] = arr[i]
        size = max(size, lo + 1)
    return size


# 测试使用
# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内 包含两个边界
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    arr1 = [52, 90, 86, 7, 52, 66, 50, 19, 78, 22, 76, -1, 60, 52, 55, 10, 51, 99, 12, 4]
    print(Maxstrway1(arr1))
    print(Maxstrway2(arr1))
    print(Maxstrway3(arr1))
    # print("----------------")
    # for _ in range(100000):
    #     arr1 = generateArray(10, -2, 100)
    #     if Maxstrway1(arr1) != Maxstrway2(arr1) or Maxstrway3(arr1) != Maxstrway2(arr1):
    #         print("出错！")
    #         print(arr1)
    #         break
    # print("成功！")
