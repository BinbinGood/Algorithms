# 给定一个数组arr，求差值为k的去重数字对。

def numpair(arr, k):
    hashset = set()
    resmap = []
    for i in arr:
        hashset.add(i)
    for i in range(len(hashset)):
        if arr[i] + k in hashset:
            resmap.append([arr[i], arr[i] + k])
        if arr[i] - k in hashset:
            resmap.append([arr[i], arr[i] + k])
    return resmap
