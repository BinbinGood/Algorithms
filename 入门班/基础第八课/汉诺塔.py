def hanoi(n):
    if n < 1:
        return
    process(n, '左', '右', '中')


# i 表示移动i层的汉诺塔的问题
# froms表示从那根柱子出发
# to 表示移动到哪根柱子结束
# other表示辅助用的柱子
def process(i, froms, to, other):
    if i == 1:
        print(f"把1从{froms}移到{to}")
    else:
        process(i - 1, froms, other, to)
        print(f"把{i}从{froms}移到{to}")
        process(i - 1, other, to, froms)


if __name__ == "__main__":
    hanoi(3)
