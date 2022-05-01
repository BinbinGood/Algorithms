# 在数组中想找到一个数，左边和右边比这个数小、且离这个数最近的位置。
# 如果对每一个数都想求这样的信息，能不能整体代价达到O(N)？
import random


# 此函数处理的是数组中没有重复值
def getNearLessNoRepeat(arr):
    res = [None] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            popIndex = stack.pop()
            if stack:
                res[popIndex] = [stack[-1], i]
            else:
                res[popIndex] = [-1, i]
        stack.append(i)
    while stack:
        popIndex = stack.pop()
        if stack:
            res[popIndex] = [stack[-1], -1]
        else:
            res[popIndex] = [-1, -1]
    return res


# 此函数处理有重复值的情况
def getNearLess(arr):
    res = [None] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1][0]] > arr[i]:
            popslist = stack.pop()
            if stack:
                leftLessIndex = stack[-1][len(stack[-1]) - 1]
            else:
                leftLessIndex = -1
            for popi in popslist:
                res[popi] = [leftLessIndex, i]
        if stack and arr[stack[-1][0]] == arr[i]:
            stack[-1].append(i)
        else:
            stack.append([i])
    while stack:
        popslist = stack.pop()
        if stack:
            leftLessIndex = stack[-1][len(stack[-1]) - 1]
        else:
            leftLessIndex = -1
        for popi in popslist:
            res[popi] = [leftLessIndex, -1]
    return res


# 测试
def getRandomArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


# 暴力遍历，复杂度O(N^2)
def rightway(arr):
    res = []
    for i in range(len(arr)):
        leftLessIndex = rightLessIndex = -1
        cur = i - 1
        while cur >= 0:
            if arr[cur] < arr[i]:
                leftLessIndex = cur
                break
            cur -= 1
        cur = i + 1
        while cur < len(arr):
            if arr[cur] < arr[i]:
                rightLessIndex = cur
                break
            cur += 1
        res.append([leftLessIndex, rightLessIndex])
    return res


def isEqual(list1, list2):
    if len(list2) != len(list1):
        return False
    for i in range(len(list1)):
        if list1[i][0] != list2[i][0] or list1[i][1] != list2[i][1]:
            return False
    return True


if __name__ == "__main__":
    str1 = [5, 4, 6, 7, 2, 3, 0, 1]
    print("-------无重复数组测试-------")
    print(getNearLessNoRepeat(str1))
    print("------有重复数字测试--------")
    str2 = [5, 4, 3, 4, 5, 3, 5, 6]
    print(getNearLess(str2))
    print("-------比较器测试------")
    min = 0
    max = 100
    l = 20
    for i in range(10000):
        list = getRandomArray(l, min, max)
        if isEqual(rightway(list), getNearLess(list)) is False:
            print("错误！")
            print(f"出错字符串：{list}")
            break
    print("成功！")
