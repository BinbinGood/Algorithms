# 给定一个只由 0(假)、1(真)、&(逻辑与)、|(逻辑或)和^(异或)五种字符组成
# 的字符串express，再给定一个布尔值 desired。返回express能有多少种组合
# 方式，可以达到desired的结果。
# 【举例】
# express="1^0|0|1"，desired=false
# 只有 1^((0|0)|1)和 1^(0|(0|1))的组合可以得到 false，返回 2。
# express="1"，desired=false
# 无组合则可以得到false，返回0

def isvaild(express):
    if (len(express) & 1) == 0:  # 偶数直接返回False
        return False
    for i in range(0, len(express), 2):
        if (express[i] != '1') and (express[i] != '0'):
            return False
    for i in range(1, len(express), 2):
        if express[i] != '&' and express[i] != '|' and express[i] != '^':
            return False
    return True


def nums1(express, desired):
    if isvaild(express) is False:
        return 0
    return process(express, desired, 0, len(express) - 1)


def process(express, desired, L, R):
    if L == R:
        if desired:
            return 1 if express[L] == '1' else 0
        else:
            return 0 if express[L] == '1' else 1
    res = 0
    if desired:
        for i in range(L + 1, R, 2):  # 此处右边界只能是R，不能是R-1。因为range(a,b)的取值不包括右边界
            if express[i] == '&':
                res += process(express, True, L, i - 1) * process(express, True, i + 1, R)
            elif express[i] == '|':
                res += process(express, True, L, i - 1) * process(express, True, i + 1, R)
                res += process(express, True, L, i - 1) * process(express, False, i + 1, R)
                res += process(express, False, L, i - 1) * process(express, True, i + 1, R)
            else:
                res += process(express, False, L, i - 1) * process(express, True, i + 1, R)
                res += process(express, True, L, i - 1) * process(express, False, i + 1, R)
    else:
        for i in range(L + 1, R, 2):
            if express[i] == '&':
                res += process(express, False, L, i - 1) * process(express, False, i + 1, R)
                res += process(express, False, L, i - 1) * process(express, True, i + 1, R)
                res += process(express, True, L, i - 1) * process(express, False, i + 1, R)
            elif express[i] == '|':
                res += process(express, False, L, i - 1) * process(express, False, i + 1, R)
            else:
                res += process(express, False, L, i - 1) * process(express, False, i + 1, R)
                res += process(express, True, L, i - 1) * process(express, True, i + 1, R)
    return res


def nums2(express, desired):
    if isvaild(express) is False:
        return 0
    tdp = [[0] * (len(express)) for _ in range(len(express))]
    fdp = [[0] * (len(express)) for _ in range(len(express))]
    for i in range(0, len(express), 2):
        tdp[i][i] = 1 if express[i] == '1' else 0
        fdp[i][i] = 0 if express[i] == '1' else 1
    for L in range(len(express) - 3, -1, -2):  # L倒叙填表
        for R in range(L - 2, len(express), 2):  # R正序填表，但是这个表对角线左下位置是无效的，且对角线已经填过了，所以从L-2位置开始
            for i in range(L + 1, R, 2):  # 此处右边界只能是R，不能是R-1。因为range(a,b)的取值不包括右边界
                if express[i] == '&':
                    tdp[L][R] += tdp[L][i - 1] * tdp[i + 1][R]
                    fdp[L][R] += fdp[L][i - 1] * fdp[i + 1][R] \
                                 + fdp[L][i - 1] * tdp[i + 1][R] \
                                 + tdp[L][i - 1] * fdp[i + 1][R]
                elif express[i] == '|':
                    tdp[L][R] += tdp[L][i - 1] * tdp[i + 1][R] \
                                 + fdp[L][i - 1] * tdp[i + 1][R] \
                                 + tdp[L][i - 1] * fdp[i + 1][R]
                    fdp[L][R] += fdp[L][i - 1] * fdp[i + 1][R]
                else:
                    tdp[L][R] += tdp[L][i - 1] * fdp[i + 1][R] + \
                                 fdp[L][i - 1] * tdp[i + 1][R]
                    fdp[L][R] += fdp[L][i - 1] * fdp[i + 1][R] + \
                                 tdp[L][i - 1] * tdp[i + 1][R]
    return tdp[0][len(express) - 1] if desired else fdp[0][len(express) - 1]


express = '1^0&0|1&1^0&0^1|0|1&1'
desired = True
print(nums1(express, desired))
print(nums2(express, desired))
