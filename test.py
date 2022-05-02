def isValid(code: str) -> bool:
    i = 1
    if code[0] != '<':
        return False
    while 1:
        if ord('A') <= ord(code[i]) <= ord('Z'):
            i += 1
        elif code[i] == '>':
            break
        else:
            return False
    if i == 1 or i > 10:
        return False
    tagname = code[1:i]  # 获取标签
    endtagname = code[-(len(tagname) + 3):]
    tagcontent = code[i + 1:-(len(tagname) + 3)]
    # print(tagname,endtagname)
    if (endtagname[:2] != '</') or (endtagname[-1] != '>') or (endtagname[2:-1] != tagname):
        return False
    # print(tagcontent)
    return tagcontentisvalid(tagcontent)


# 判断中间的字符串是否有效
def tagcontentisvalid(strs):
    flag = -1
    i = 0
    cdata = '<![CDATA['
    while i < len(strs):
        if i + len(cdata) <= len(strs) and (strs[i:i + len(cdata)] == cdata):
            flag = i  # cdata开始的下标
            break
        i += 1
    if flag == -1:
        return False
    i = flag + len(cdata)  # cdata_content开始的位置
    while i < len(strs):
        if ((i + 3) <= len(strs)) and (strs[i:i + 3] == ']]>'):
            break
        i += 1
    if i == len(strs):
        return False
    i += 3
    if flag == 0 and i == len(strs) - 1:  # 只有cdata没有任意字符
        return False
    return True


str1 = "<DIV>  div tag is not closed  <DIV>"
print(isValid(str1))
