def process(str1, i, res):
    if i == len(str1):
        res.append(str1[:])  # 一定要把列表复制一份，不然对应的内存映射相同。最终结果不变
        return
    visit = [False] * 26
    for j in range(i, len(str1), 1):
        if visit[ord(str1[j]) - ord('a')] is False:
            visit[ord(str1[j]) - ord('a')] = True
            swap(str1, j, i)
            process(str1, i + 1, res)
            swap(str1, j, i)


def swap(str2, j, i):
    temp = str2[i]
    str2[i] = str2[j]
    str2[j] = temp


if __name__ == "__main__":
    str1 = 'abc'
    strlist1 = []
    for i in range(len(str1)):
        strlist1.append(str1[i])
    result = []
    print("---------")
    process(strlist1, 0, result)
    print(result)
