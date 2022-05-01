# 给定一个整数数组A，长度为n，有 1 <= A[i] <= n，且对于[1,n]的整数，其
# 中部分整数会重复出现而部分不会出现。
# 实现算法找到[1,n]中所有未出现在A中的整数。
# 提示：尝试实现O(n)的时间复杂度和O(1)的空间复杂度（返回值不计入空间复
# 杂度）。
# 输入描述：
# 一行数字，全部为整数，空格分隔
# A0 A1 A2 A3... 输出描述：
# 一行数字，全部为整数，空格分隔R0 R1 R2 R3... 示例1:
# 输入
# 1 3 4 3
# 输出
# 2

def noinarray(A):
    if len(A) < 1:
        return
    for i in range(len(A)):
        modify(A, A[i])
    for i in range(len(A)):
        if A[i] != i + 1:
            print(i + 1, end=' ')


def modify(array, value):
    while array[value - 1] != value:
        temp = array[value - 1]
        array[value - 1] = value
        value = temp


arr1 = [1, 3, 4, 5, 7, 4, 3]
noinarray(arr1)
