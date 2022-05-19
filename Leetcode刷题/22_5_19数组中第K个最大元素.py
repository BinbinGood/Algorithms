import random


def findKthLargest(nums, k: int) -> int:
    def quicksort(nums, l, r):
        if l == r:
            return nums[l]
        left, right = sort(nums, l, r)
        if len(nums) - right - 1 < k <= len(nums) - left:
            return nums[left]
        elif len(nums) - right - 1 >= k:
            return quicksort(nums, right + 1, r)
        else:
            return quicksort(nums, l, left - 1)

    return quicksort(nums, 0, len(nums) - 1)


def sort(nums, l, r):
    leftindex = l
    rightindex = r - 1
    num = nums[r]
    i = l
    while i <= rightindex:
        if nums[i] == num:
            i += 1
        elif nums[i] < num:
            temp = nums[leftindex]
            nums[leftindex] = nums[i]
            nums[i] = temp
            i += 1
            leftindex += 1
        else:
            temp = nums[rightindex]
            nums[rightindex] = nums[i]
            nums[i] = temp
            rightindex -= 1
    temp = nums[rightindex + 1]
    nums[rightindex + 1] = nums[r]
    nums[r] = temp
    return (leftindex, rightindex + 1)

# def generateArray(l, minsize, maxsize):
#     genarray = []
#     for i in range(l):
#         genarray.append(random.randint(minsize, maxsize))
#     return genarray
#
#
# arr = generateArray(20, -10, 100)
# quicksort(arr, 0, len(arr) - 1)
# print(arr)
