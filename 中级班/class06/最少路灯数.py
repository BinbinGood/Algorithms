# 小Q正在给一条长度为n的道路设计路灯安置方案。
# 为了让问题更简单,小Q把道路视为n个方格,需要照亮的地方用'.'表示, 不需要
# 照亮的障碍物格子用'X'表示。小Q现在要在道路上设置一些路灯, 对于安置在
# pos位置的路灯, 这盏路灯可以照亮pos - 1, pos, pos + 1这三个位置。
# 小Q希望能安置尽量少的路灯照亮所有'.'区域, 希望你能帮他计算一下最少需
# 要多少盏路灯。
# 输入描述：
# 输入的第一行包含一个正整数t(1 <= t <= 1000), 表示测试用例数
# 接下来每两行一个测试数据, 第一行一个正整数n(1 <= n <= 1000),表示道路
# 的长度。第二行一个字符串s表示道路的构造,只包含'.'和'X'。
# 输出描述：
# 对于每个测试用例, 输出一个正整数表示最少需要多少盏路灯。

def MinLight(arr):
    light = 0
    index = 0
    while index != len(arr):
        if arr[index] == 'X':
            index += 1
        else:
            light += 1
            if index + 1 == len(arr):  # 越界直接跳出
                break
            else:
                if arr[index + 1] == 'X':  # 如果index+1不越界，切为'X'
                    index = index + 2
                else:  # index,index+1全是‘.’的情况，这时候无论index+2是什么都可以直接跳到index+3处理
                    index = index + 3
    return light


