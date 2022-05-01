# 给定一个数组arr，长度为N且每个值都是正数，代表N个人的体重。再给定一个正数
# limit，代表一艘船的载重。以下是坐船规则，1）每艘船最多只能做两人；2）乘客
# 的体重和不能超过limit。返回如果同时让这N个人过河最少需要几条船。

def Minboat(arr1, limit):
    if len(arr1) == 0 or limit < 0:
        return 0
    for i in range(len(arr1)):
        if arr1[i] > limit:
            return None
    arr1.sort()  # 从小打到进行排序
    if arr1[len(arr1) - 1] < limit / 2:
        return (len(arr1) + 1) // 2  # 向上取整
    if arr1[0] > limit / 2:
        return len(arr1)

    # 找到中点位置
    mid = len(arr1) - 1
    while mid >= 0:
        if arr1[mid] > limit / 2:
            mid -= 1
        else:
            break
    # 从中点开始向两边扩
    L, R = mid, mid + 1
    unsolve = 0  # 小于中位数中，没办法和大于中位数拼船的人数
    ok = 0  # 贪心，小于中位数中，可以拼船的人数
    while L >= 0:
        if arr1[L] + arr1[R] > limit:
            unsolve += 1
            L -= 1
        else:
            ok += 1
            L -= 1
            R += 1
    return (unsolve + 1) // 2 + ok + len(arr1) - R


arr1 = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
weight = 5
print(Minboat(arr1, weight))
