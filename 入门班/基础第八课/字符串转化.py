def transformerstrings(str, i):
    if len(str) == i:
        return 1
    if str[i] == '0':
        return 0
    if str[i] == '2':
        res = transformerstrings(str, i + 1)
        if (i + 1 < len(str)) and (str[i + 1] >= '0') and (str[i + 1] <= '6'):
            res += transformerstrings(str, i + 2)
        return res
    if str[i] == '1':
        res = transformerstrings(str, i + 1)
        if i + 1 < len(str):
            res += transformerstrings(str, i + 2)
        return res
    return transformerstrings(str, i + 1)


if __name__ == "__main__":
    str1 = '111'
    print(transformerstrings(str1, 0))
    print(chr(ord('A')+1))
