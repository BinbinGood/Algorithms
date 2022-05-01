from heapq import heappop, heappush


# heap = []            # creates an empty heap
# heappush(heap, item) # pushes a new item on the heap
# item = heappop(heap) # pops the smallest item from the heap
# item = heap[0]       # smallest item on the heap without popping it
# heapify(x)           # transforms list into a heap, in-place, in linear time
# item = heapreplace(heap, item) # pops and returns smallest item, and adds
#                                # new item; the heap size is unchanged

def DictanceLessK(arr, K):
    if len(arr) < 2 or K < 2:
        return
    heap = []
    index = 0
    while index < min(len(arr), K):
        heappush(heap, arr[index])
        index += 1
    i = 0
    while index < len(arr):
        heappush(heap, arr[index])
        arr[i] = heappop(heap)
        index += 1
        i += 1

    while len(heap) != 0:
        arr[i] = heappop(heap)
        i += 1


if __name__ == "__main__":
    array = [3, 2, 1, 8, 5, 6, 7, 4, 9, 10]
    print(array)
    DictanceLessK(array, 3)
    print(array)
    # hq=[]
    # heappush(hq, 1)
    # heappush(hq, 3)
    # heappush(hq, 4)
    # heappush(hq, 2)
    # heappush(hq, 7)
    # print(f"堆的heapsize为：len(hq)")
    # for i in range(len(hq)):
    #     print(heappop(hq))
    # print(f"全部弹出以后堆的heapsize为：len(hq)")
