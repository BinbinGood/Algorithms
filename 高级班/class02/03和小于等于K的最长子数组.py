# 给定一个无序数组 arr，其中元素可正、可负、可 0，给定一个整数 k。求 arr 所
# 有的子数组 中累加和小于或等于 k 的最长子数组长度。
# 例如:arr=[3,-2,-4,0,6]，k=-2，相加和小于或等于-2 的最长子数组为{3,-2,-
# 4,0}，所以结果返回4。

def Maxlongarr(arr, k):
    minsum = [0] * len(arr)
    minsumend = [0] * len(arr)
    minsum[len(arr) - 1] = arr[len(arr) - 1]
    minsumend[len(arr) - 1] = len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        minsum[i] = arr[i]
        if minsum[i + 1] <= 0:
            minsum[i] += minsum[i + 1]
        minsumend[i] = minsumend[i + 1] if minsum[i + 1] <= 0 else i

    end = 0
    sum = 0  # 计算累加和
    res = 0  # 保存最终的结果
    # i是窗口的最左的位置，end是窗口最右位置的下一个位置
    for i in range(len(arr)):
        # while循环结束之后：
        # 1) 如果以i开头的情况下，累加和 <= k的最长子数组是arr[i..end - 1]，看看这个子数组长度能不能更新res；
        # 2) 如果以i开头的情况下，累加和 <= k的最长子数组比arr[i..end - 1]短，更新还是不更新res都不会影响最终结果；
        while end < len(arr) and sum + minsum[end] <= k:  # 找到以当前位置i开始的数组累加和小于等于K的最大长度
            sum += minsum[end]  # 进入循环表示当前块加入以后还小于等于K
            end = minsumend[end] + 1
        res = max(res, end - i)  # 更新最大值
        if end > i:  # 窗口还有数
            sum -= arr[i]
        else:  # 表示窗口已经没有数了，
            end = i + 1

    return res


arr = [3, -2, -4, 0, 6]
k = -2
print(Maxlongarr(arr, k))
