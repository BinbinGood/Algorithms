def Manacher(s):
    if s is None or len(s) < 1:
        return 0
    str = manacherString(s)
    # print(str)
    pstr = [0] * len(str)  # 回文半径数组
    R = C = -1  # 回稳右边界的再往右一个位置，最右的有效区是R-1位置
    maxstr = -1
    for i in range(len(str)):
        # 确定至少不用验的区域，包含了四种情况
        if R > i:
            pstr[i] = min((R - i), pstr[2 * C - i])
        else:
            pstr[i] = 1
        # 把这四种情况都在上述不用验的基础上尝试往外扩
        while (i + pstr[i] < len(str)) and (i - pstr[i] > -1):
            if str[i + pstr[i]] == str[i - pstr[i]]:
                pstr[i] += 1
            else:
                break
        # 更新最右回文的右边界和此时中心点的位置
        if (i + pstr[i]) > R:
            R = i + pstr[i]
            C = i
        # 更新最大回文串长度
        maxstr = max(maxstr, pstr[i])
    # print(pstr)
    return maxstr - 1


def manacherString(s):
    for i in range(len(s) - 1, -1, -1):
        s = s[:i + 1] + '#' + s[i + 1:]
        # print(s)
    str = '#' + s
    return str


if __name__ == "__main__":
    str1 = 'abccabccbabcc'
    print(Manacher(str1))
