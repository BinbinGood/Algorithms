# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
import math


def numSubarrayProductLessThanK(nums, k):
    if k == 0:
        return 0
    # 二分法
    helpnums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        helpnums[i + 1] = math.log(nums[i]) + helpnums[i]
    ans = 0
    for i in range(1, len(nums) + 1):  # 以i为右边界
        # 利用二分法，找到0到i区间内，第一个满足helpnums[l]>helpnums[i]-log(k)。的坐标k
        val = helpnums[i] - math.log(k)
        l, r = 0, i
        while l < r:
            mid = (l + r) // 2
            if helpnums[mid] > val:
                r = mid
            else:
                l = mid + 1
        ans += i - r
    return ans


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))

# # 写一个二分法模板，找到第一个大于k的下标
# def erfen(arr, k):
#     l, r = 0, len(arr) - 1
#     while l < r:
#         mid = (l + r) // 2
#         if arr[mid] > k:
#             r = mid
#         else:
#             l = mid + 1
#     return r
#
#
# print(erfen([1, 1.2, 1.5, 2, 3, 4, 4.1, 4.6, 5, 5, 7.9, 10, 45, 56], 5))
