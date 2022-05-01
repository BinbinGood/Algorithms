# 给定一个全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，并让
# 最终结果字符串的字典序最小
# 【举例】
# str = "acbc"，删掉第一个'c'，得到"abc"，是所有结果字符串中字典序最小的。
# str = "dbcacbca"，删掉第一个'b'、第一个'c'、第二个'c'、第二个'a'，得到"dabc"，
# 是所有结 果字符串中字典序最小的。

def removeDuplicateLetters(str1):
    map = [0] * len(str1)
    for i in range(len(str1)):  # 统计所有字符的词频，没有的就是0
        map[ord(str1[i]) - ord('a')] += 1
    res = ''  # 存放结果
    L, R = 0, 0  # 用来表示开始和结束的指针
    while R != len(str1):
        if map[ord(str1[R]) - ord('a')] == 0:
            print(str1[R])
        if map[ord(str1[R]) - ord('a')] > 0:  # 如果某个字符的词频大于0
            map[ord(str1[R]) - ord('a')] -= 1  # 自减一
        # 若某个元素的词频为-1 表示此字符已经放入结果数组中了，不需要计算直接跳过，继续往前走。
        # 若某个元素再自减一以后还是大于零，表示后续还有字符，可以继续走
        if map[ord(str1[R]) - ord('a')] == -1 or map[ord(str1[R]) - ord('a')] > 0:
            R += 1
        else:  # 反之，遇到若某元素词频为0，表示后续没有该元素了，则需要在此时的L到R的范围上提取出最小字典序的字符
            pick = -1
            for i in range(L, R + 1, 1):
                if map[ord(str1[i]) - ord('a')] != -1 and (pick == -1 or (ord(str1[i]) < ord(str1[pick]))):
                    pick = i
            # 最后pick中保存的即为最小ASCALL码的字符位置，将其放入结果字符中。同时将该字符的词频修改为-1 ，表示后续不在考虑该字符
            res += str1[pick]
            map[ord(str1[pick]) - ord('a')] = -1
            # 将pick到R范围上字符的词频重新记录到词频表中
            for i in range(pick + 1, R + 1, 1):
                if map[ord(str1[i]) - ord('a')] != -1:
                    map[ord(str1[i]) - ord('a')] += 1
            # 更新L和R的范围
            L = pick + 1
            R = L
    return res


str1 = "acbc"
print(removeDuplicateLetters(str1))
