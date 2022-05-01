# 在一个有序数组中找出某个数是否存在
def FindNum(arrs, num):
    if len(arrs) < 2:
        return False
    hi = len(arrs) - 1
    lo = 0
    while lo < hi:
        mid = int(lo + (hi - lo) / 2)  # 这样写防止溢出
        if arrs[mid] == num:
            return True
        elif arrs[mid] > num:
            hi = mid - 1
        elif arrs[mid] < num:
            lo = mid + 1
    return arrs[lo] == num


# 在一个有序数组中找到小于等于num的最左侧的位置
def FindNumLeft(arrs, num):
    if len(arrs) < 2:
        return False
    hi = len(arrs) - 1  # 高位
    lo = 0  # 低位
    p1 = -1  # 记录此时的中间位置
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)  # 这样写防止溢出
        if arrs[mid] >= num:
            p1 = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return p1


if __name__ == "__main__":
    sortarray = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
    index = FindNum(sortarray, 12)
    print(FindNumLeft(sortarray, 7))
    print(index)
