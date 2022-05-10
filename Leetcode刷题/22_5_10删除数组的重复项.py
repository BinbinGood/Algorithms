# 80题
def removeDuplicates(nums):
    # slow保存有效的数据
    slow = 2  # 保存有效数组的长度
    fast = 2  # fast从左往右移动，查看每一个元素
    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:  # 如果当前元素和有效数据的倒数第二个不相等
            # 表示重复数据不超过2，可以将其纳入有效数据中
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
