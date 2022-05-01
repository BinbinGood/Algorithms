# 定义：数组中累积和与最小值的乘积，假设叫做指标A。
# 给定一个数组，请返回子数组中，指标A最大的值。
# 暴力遍历
import random


def max1(arr):
    max1 = -1  # 假设没有负数
    for i in range(len(arr)):
        for j in range(i, len(arr), 1):
            minnum = 1000000  # 假设最大值不超过100万
            sum = 0
            for k in range(i, j + 1, 1):
                sum += arr[k]
                minnum = min(minnum, arr[k])
            max1 = max(max1, minnum * sum)
    return max1


# 使用单调栈，O（N）
def max2(arr):
    sums = []
    # 计算每个元素的 前0~i项 之和
    sums.append(arr[0])
    for i in range(1, len(arr), 1):
        sums.append(sums[-1] + arr[i])
    # print(sums)
    max2 = -1
    stack = []  # 小底栈
    for i in range(len(arr)):
        while stack and (arr[stack[-1]] >= arr[i]):
            j = stack.pop()
            if stack:
                # 第i项大于此时的弹出元素，所以计算的是前i-1项元素和，如果左边有比i项小的项，则要减去比i小的项的和。然后乘以最小值arr[j]
                cur = (sums[i - 1] - sums[stack[-1]]) * arr[j]
            else:
                cur = sums[i - 1] * arr[j]
            max2 = max(max2, cur)
        stack.append(i)
    while stack:
        j = stack.pop()
        if stack:
            # 此时右边无界，所以是第i项的前n项和
            cur = (sums[- 1] - sums[stack[-1]]) * arr[j]
        else:
            cur = sums[- 1] * arr[j]
        max2 = max(max2, cur)
    return max2


# 测试
def getRandomArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    str1 = [91, 31, 6, 32, 55]
    print(max1(str1))
    print(max2(str1))

    print("------比较器------")
    for i in range(10000):
        list = getRandomArray(20, 0, 100)
        if max1(list) != max2(list):
            print("错误！")
            print(f"出错的数组:{list}")
            break
    print("成功！")
