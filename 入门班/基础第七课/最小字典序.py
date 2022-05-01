# 给定一个字符串类型的数组strs，找到一种拼接方式，使得把所有字符串拼起来之后形成的
# 字符串具有最小的字典序。
import functools


# 自定义的比较器
# 按照a+b<b+a的方式排序
def MyComparator(a, b):
    if (a + b) < (b + a):
        return -1
    elif (a + b) > (b + a):
        return 1
    else:
        return 0


def lowestString(strs):
    if (strs is None) or len(strs) == 0:
        return ''
    strs.sort(key=functools.cmp_to_key(MyComparator))
    res = ""
    for i in strs:
        res += i
    return res


if __name__ == "__main__":
    str1 = ["jibw", "ji", "jp", "bw", "jibw"]
    # str1 = ["ba", "b", "c", "cd"]
    str1 = lowestString(str1)
    print("排序后的结果")
    print(str1)
