# 给定一个有序数组arr，代表数轴上从左到右有n个点arr[0]、arr[1]...arr[n－1]，
# 给定一个正数L，代表一根长度为L的绳子，求绳子最多能覆盖其中的几个点。

# 滑动窗口法
def MaxPoints(arr, L):
    if len(arr) < 1 or L < 1:
        return 0
    maxpoint = 1
    low, high = 0, 0
    while high != len(arr):
        if (arr[high] - arr[low]) <= L:
            high += 1
        else:
            maxpoint = max(maxpoint, high - low)
            low += 1
    maxpoint = max(maxpoint, high - low)
    return maxpoint


# 二分法
def MaxPoints2(arr, L):
    if len(arr) < 1 or L < 1:
        return 0
    res = 1
    for i in range(len(arr)):
        nearest = FindNumLeft(arr, i, arr[i] - L)
        res = max(res, i - nearest + 1)
    return res


# 在一个有序数组中找到小于等于num的最左侧的位置
# 在arr[0..R]范围上，找满足>=value的最左位置
def FindNumLeft(arrs, R, num):
    if len(arrs) < 2:
        return False
    lo = 0  # 低位
    p1 = R  # 记录此时的中间位置
    while lo < R:
        mid = int(lo + (R - lo) / 2)  # 这样写防止溢出
        if arrs[mid] >= num:
            p1 = mid
            R = mid - 1
        else:
            lo = mid + 1
    return p1


if __name__ == "__main__":
    str1 = [2, 4, 8, 9, 12, 17]
    str2 = [0, 13, 24, 35, 46, 57, 60, 72, 87]
    print(MaxPoints(str1, 1))
    print(MaxPoints2(str1, 1))
    print(MaxPoints(str2, 1))
    print(MaxPoints2(str2, 1))
