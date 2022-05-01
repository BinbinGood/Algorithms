# 给定一个数组arr长度为N，你可以把任意长度大于0且小于N的前缀作为左部分，剩下的
# 作为右部分。但是每种划分下都有左部分的最大值和右部分的最大值，请返回最大的，
# 左部分最大值减去右部分最大值的绝对值。


def Maxleftright(arr):
    if len(arr) < 3:
        return 0
    maxnum = arr[0]
    for i in range(1, len(arr) - 1, 1):
        maxnum = max(maxnum, arr[i])
    return maxnum - min(arr[0], arr[len(arr) - 1])
