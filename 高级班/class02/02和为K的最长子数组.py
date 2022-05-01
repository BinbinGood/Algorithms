# 给定一个数组 arr，该数组无序，但每个值均为正数，再给定一个正数 k。求 arr 的
# 所有子 数组中所有元素相加和为 k 的最长子数组长度。
# 例如，arr=[1,2,1,1,1]，k=3。
# 累加和为 3 的最长子数组为[1,1,1]，所以结果返回 3。
# 要求：时间复杂度O(N)，额外空间复杂度O(1)


# 使用滑动窗口，当前窗口内的和大于k时l右移，小于K时R右移。当等于K时更新最大长度
def Maxlongarr(arr, k):
    res = 0
    L = R = 0
    lrsum = arr[0]
    while R < len(arr):
        if lrsum < k:
            R += 1
            if R<len(arr):
                lrsum += arr[R]
        elif lrsum > k:
            L += 1
            lrsum -= arr[L - 1]
        else:
            res = max(res, (R - L + 1))
            L += 1
            lrsum -= arr[L - 1]
    return res

arr1 = [5,5,1,1,1]
k = 3
print(Maxlongarr(arr1,k))
