# 给定两个一维int数组A和B.
# 其中：A是长度为m、元素从小到大排好序的有序数组。B是长度为n、元素从小
# 到大排好序的有序数组。希望从A和B数组中，找出最大第k个数字，要求：使用
# 尽量少的比较次数

def findKthNum(arr1, arr2, k):
    if len(arr1) == 0 or len(arr2) == 0:
        return
    if k < 1 or k > (len(arr2) + len(arr1)):
        return
    longs = arr1 if len(arr2) < len(arr1) else arr2
    shorts = arr2 if longs == arr1 else arr1
    if k <= len(shorts):  # 情况一，k小于短数组的长度；此时直接调用求上中位数的算法即可
        return getupMedian(shorts, 0, k - 1, longs, 0, k - 1)
    if k > len(longs):  # 情况二，k大于长数组的长度；此时要先判断两个边界是否符合条件，符合直接返回，否则调用剩余区间内的上中位数算法
        if shorts[k - len(longs) - 1] >= longs[len(longs) - 1]:
            return shorts[k - len(longs) - 1]
        if longs[k - len(shorts) - 1] >= shorts[len(shorts) - 1]:
            return longs[k - len(shorts) - 1]
        return getupMedian(shorts, k - len(longs), len(shorts) - 1, longs, k - len(shorts), len(longs) - 1)
    else:  # 情况三，k大于短数组的长度，小于等于长数组的长度；此时有一个边界要进行判断，那就是长数组的第k-len(shorts)这一位的值是否比短数组最后一位大，
        # 若大于等于则直接返回该值。否则调用算法
        if longs[k - len(shorts) - 1] >= shorts[len(shorts) - 1]:
            return longs[k - len(shorts) - 1]
        return getupMedian(shorts, 0, len(shorts) - 1, longs, k - len(shorts), k - 1)


# 该算法原型要求a1和a2等长
# 对于他们的长度分为奇数和偶数。
# 当中位数相等时，无论奇数还是偶数长度都直接返回中位数即可。
# 当为偶数时：且a1[mid1]>a2[mid2]。则上中位数一定存在与a1[s1,mid1]和a2[mid2+1,e2]中间。
# 当为奇数时：且a1[mid1]>a2[mid2]。则上中位数一定存在于a1[s1,mid1]和a2[mid2,s2]中间。
def getupMedian(a1, s1, e1, a2, s2, e2):
    if len(a1) != len(a2):
        return 0
    mid1, mid2 = 0, 0
    offset = 0  # 用来判断长度为奇还是偶。奇数为0，偶数为1
    while s1 < e1:
        mid1, mid2 = (s1 + e1) // 2, (s2 + e2) // 2
        offset = ((e1 - s1 + 1) & 1) ^ 1
        if a1[mid1] > a2[mid2]:
            e1 = mid1
            s2 = mid2 + offset
        elif a1[mid1] > a2[mid2]:
            s1 = mid1 + offset
            e2 = mid2
        else:
            return a1[mid1]
    return min(a1[s1], a2[s2])
