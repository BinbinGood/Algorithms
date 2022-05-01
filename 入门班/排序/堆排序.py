# 堆结构是一种优先级队列
import random


def HeapSort(arr):
    if len(arr) < 2:
        return
    # # 这种从上到下构造最大堆的方式时间复杂度位O(N*logN)
    # 一个一个添加元素，形成大根堆
    # for i in range(len(arr)):
    #     heapInsert(arr, i)
    # 下面这种从下到上的方法构造最大堆的方式时间复杂度为O(N)
    #
    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, i, len(arr))
    # 把堆的最大值和堆末尾的值交换，然后减少堆的大小之后，再去调
    # 整堆，一直周而复始，时间复杂度为O(N*logN)
    heapsize = len(arr)
    heapsize -= 1
    swap(arr, 0, heapsize)
    while heapsize > 0:
        heapify(arr, 0, heapsize)
        heapsize -= 1
        swap(arr, 0, heapsize)


def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:  # 所有它的值大于父亲的值，则交换
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def heapify(arr, index, size):
    left = 2 * index + 1
    while left < size:
        # 在保证左右子节点不越界的情况下，找到两个子节点的最大值,若有右节点则判断右节点是否为最大值
        if left + 1 < size and arr[left + 1] > arr[left]:
            largest = left + 1
        else:
            largest = left
            # 如果小于该位置的值，则跳出循环
        if arr[index] >= arr[largest]:
            break
        # 否则交换位置，继续往下比较
        swap(arr, index, largest)
        index = largest
        left = 2 * index + 1


def swap(arr, a, b):
    tem = arr[a]
    arr[a] = arr[b]
    arr[b] = tem


# 此函数将产生一个长度为L的数组，数组元素大小在minsize到maxsize范围内
def generateArray(l, minsize, maxsize):
    genarray = []
    for i in range(l):
        genarray.append(random.randint(minsize, maxsize))
    return genarray


if __name__ == "__main__":
    # array = generateArray(20, 0, 100)
    # print(array)
    # HeapSort(array)
    # print(array)

    times = 10000
    succedflag = True
    for time in range(times):
        array = generateArray(50, 0, 100)
        array1 = array[:]
        HeapSort(array)
        array1.sort()
        if array1 != array:
            print("出错")
            succedflag = False
            print(array1)
            print(array)
            break
    if succedflag:
        print("成功")