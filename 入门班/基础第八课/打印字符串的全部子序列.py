# 方案一
def printAllSubsquence(str):
    if len(str) < 1:
        return
    res = ''
    process(0, str, res)


def process(i, str, res):
    if i == len(str):
        print(res)
        return
    reskeep = res + str[i]
    process(i + 1, str, reskeep)
    resNoInclude = res
    process(i + 1, str, resNoInclude)


# 方案二
def printAllSubsquence2(str):
    if len(str) < 1:
        return
    process2(0, str)


def process2(i, string):
    if i == len(string):
        print(string)
        return
    process2(i + 1, string)
    temp = string[i]
    string = string[:i] + ' ' + string[i + 1:]
    process2(i + 1, string)
    string = string[:i] + temp + string[i + 1:]


if __name__ == "__main__":
    printAllSubsquence('abc')
    print("----------------")
    string = 'abc'
    printAllSubsquence2(string)
    print("----------------")
