# 给定一个数组，求如果排序之后，相邻两数的最大差值。要求时间复杂度O(N)，且要
# 求不能用非基于比较的排序。

def MaxGap(arr):
    if len(arr) < 2:
        return 0
    # 找到最大值和最小值
    maxnum = arr[0]
    minnum = arr[0]
    for i in range(1, len(arr)):
        maxnum = max(maxnum, arr[i])
        minnum = min(minnum, arr[i])
    if maxnum == minnum:
        return 0
    # 设置len(arr)+1个桶，每个桶只存放属于这个数值范围的数字的最大值和最小值，
    hasnum = [False] * (len(arr) + 1)
    maxs = [0] * (len(arr) + 1)
    mins = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        bid = buket(arr[i], len(arr), minnum, maxnum)
        mins[bid] = min(mins[bid], arr[i]) if hasnum[bid] else arr[i]
        maxs[bid] = max(maxs[bid], arr[i]) if hasnum[bid] else arr[i]
        hasnum[bid] = True

    res = 0  # 结果
    lastmax = maxs[0]  # 保存上一个桶的最大值
    for i in range(1, len(arr) + 1):
        if hasnum[i]:
            res = max(res, (mins[i] - lastmax))  # 最大差值一定存在于桶于桶之间
            lastmax = maxs[i]  # 更新上一个桶的最大值

    return res


# 根据当前的数字，整个数组的最大值和最小值已经数组的长度，计算当前数字num应该属于哪一个桶。
def buket(num, lennum, minnum, maxnum):
    return (((num - minnum) * lennum) // (maxnum - minnum))


arr = [2, 5, 7, 1, 5, 7, 9, 1, 6, 2, 0, 4, 8, 10]
print(MaxGap(arr))
