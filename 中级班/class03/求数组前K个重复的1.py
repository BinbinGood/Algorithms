# 给定一个字符串类型的数组arr，求其中出现次数最多的前K个

# 方法一：首先利用哈希表统计词频，然后利用大根堆，将所有字符和对应的词频全进大根堆，弹出前K个即可。
def PrintTopk1(arr, k):
    if len(arr) == 0 or k < 0:
        return
    numhash = dict()
    for i in range(len(arr)):
        if arr[i] in numhash:
            numhash[arr[i]] += 1
        else:
            numhash[arr[i]] = 1
    # 构建字符和对应词频的大根堆
    bigheap = []
    heapsize = 0
    for key in numhash:
        node = [key, numhash[key]]
        bigheap.append(node)
        heapInsert(bigheap, heapsize)
        heapsize += 1
    # print(bigheap)
    # print(heapsize)
    res = []
    k = min(k, len(numhash))
    for i in range(k):
        res.append(bigheap[0])  # 取出堆顶元素
        swap(bigheap, 0, heapsize - 1)
        heapsize -= 1
        heapify(bigheap, 0, heapsize)
    print(res)


# 方法二：首先利用哈希表统计词频，然后利用小根堆，创建一个大小为K的小根堆，每个字符查看小根堆堆顶的词频是否小于此字符，
# 若小于该字符，删除现在的堆顶元素，将此字符存入，使用heapify向下调整。遍历结束弹出小根堆所有元素即可。
def PrintTopk2(arr, k):
    if len(arr) == 0 or k < 0:
        return
    numhash = dict()
    for i in range(len(arr)):
        if arr[i] in numhash:
            numhash[arr[i]] += 1
        else:
            numhash[arr[i]] = 1
    # 构建大小为k的小根堆
    bigheap = []
    heapsize = 0
    for key in numhash:
        node = [key, -numhash[key]]  # 利用大根堆，只需要将存放的数修改为相反数，效果就是小根堆
        if heapsize < k:
            bigheap.append(node)
            heapInsert(bigheap, heapsize)
            heapsize += 1
        else:
            if bigheap[0][1] > node[1]:
                bigheap[0] = node
                heapify(bigheap, 0, heapsize)
    res = []
    for i in range(heapsize):
        res.append([bigheap[i][0], -bigheap[i][1]])  # 取出小根堆所有元素
    print(res)


# 向上调整
def heapInsert(heap, i):
    while heap[i][1] > heap[int((i - 1) / 2)][1]:
        swap(heap, i, int((i - 1) / 2))
        i = int((i - 1) / 2)


# 向下调整
def heapify(heap, i, size):
    left = 2 * i + 1
    while left < size:
        if left + 1 < size and heap[left + 1][1] > heap[left][1]:
            largest = left + 1
        else:
            largest = left
        if heap[i][1] >= heap[largest][1]:  # 如果小于该位置的值，则跳出循环
            break
        swap(heap, i, largest)
        i = largest
        left = 2 * i + 1


def swap(arr, a, b):
    tem = arr[a]
    arr[a] = arr[b]
    arr[b] = tem


if __name__ == "__main__":
    str1 = ['a', 'b', 'c', 'a', 'b', 'a', 'a', 'b', 'd', 'e', 'b', 'c', 'g', 'c', 'e', 'h', 'g']
    k = 3
    PrintTopk1(str1, k)
    PrintTopk2(str1, k)
