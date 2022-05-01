def printflods(N):
    printProcess(1, N, True)


# i表示节点层数，N表示总的折纸次数
# down=True表示凹，down==False表示凸
def printProcess(i, N, down):
    if i > N:
        return
    printProcess(i + 1, N, True)  # 实际是一颗二叉树，使用中序遍历
    if down:
        print("凹")
    else:
        print("凸")
    printProcess(i + 1, N, False)


if __name__ == "__main__":
    N = 3
    printflods(N)
