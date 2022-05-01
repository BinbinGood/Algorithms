# 汉诺塔游戏的要求把所有的圆盘从左边都移到右边的柱子上，给定一个整型数组arr，
# 其中只含有1、2和3，代表所有圆盘目前的状态，1代表左柱，2代表中柱，3代表右柱，
# arr[i]的值代表第i+1个圆盘的位置。
# 比如，arr=[3,3,2,1]，代表第1个圆盘在右柱上、第2个圆盘在右柱上、第3个圆盘在中
# 柱上、第4个圆盘在左柱上
# 如果arr代表的状态是最优移动轨迹过程中出现的状态，返回arr这种状态是最优移动轨
# 迹中的第几个状态；如果arr代表的状态不是最优移动轨迹过程中出现的状态，则返回-1。

def stepth1(arr):
    if len(arr) == 0:
        return -1
    return process(arr, len(arr) - 1, 1, 3, 2)  # 从1移动到3,2是辅助杆子


# 目标是：把0~i的圆盘，从f全部挪到t上,o是辅助杆子
# 返回，根据arr中的状态arr[0~i]，他是最优解的第几步？
# O(N)
def process(arr, i, f, t, o):
    if i == -1:
        return 0
    if arr[i] != f and arr[i] != t:  # 情况三
        return -1
    # arr[i] 不是form就是to
    if arr[i] == f:
        return process(arr, i - 1, f, o, t)  # 看0~i-1从f移动到o进行到了哪一步
    else:
        rest = process(arr, i - 1, o, t, f)  # 看0~i-1从o移动到t进行到了哪一步
        if rest == -1:
            return -1
        else:
            return (1 << i) + rest


# # 暴力递归改迭代
# def stepth2(arr):
#     if len(arr) == 0:
#         return -1


arr = [3, 3, 2, 1]
print(stepth1(arr))
