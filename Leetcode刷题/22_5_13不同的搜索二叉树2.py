# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateTrees(n: int):
    def process(arr):  # 从arr中返回所有节点组成的二叉搜索树,假设arr是有序的
        if len(arr) == 1:
            return [TreeNode(arr[0])]
        # if len(arr) == 0:
        #     return []
        ans = []
        for i in range(len(arr)):  # 遍历数组中的数，轮流当作头节点
            leftarr = arr[:i]
            rightarr = arr[i + 1:]
            lefttrees = process(leftarr) if leftarr else []
            righttrees = process(rightarr) if rightarr else []
            if lefttrees and righttrees:
                for left in lefttrees:
                    for right in righttrees:
                        ans.append(TreeNode(arr[i], left, right))
            elif lefttrees:
                for left in lefttrees:
                    ans.append(TreeNode(arr[i], left, None))
            else:
                for right in righttrees:
                    ans.append(TreeNode(arr[i], None, right))
        return ans

    return process([i for i in range(1, n + 1)])


treelist = generateTrees(3)
print([node.val for node in treelist])
