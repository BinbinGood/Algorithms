# 给定两个长度都为N的数组weights和values，weights[i]和values[i]分别代表
# i号物品的重量和价值。给定一个正数bag，表示一个载重bag的袋子，你装的物
# 品不能超过这个重量。返回你能装下最多的价值是多少


def process1(weights, values, i, alreadyweight, alreadyvalue, bag):
    if alreadyweight > bag:
        return 0
    if i == len(weights):
        return alreadyvalue
    return max(process1(weights, values, i + 1, alreadyweight,
                        alreadyvalue, bag),
               (process1(weights, values, i + 1, alreadyweight + weights[i],
                         alreadyvalue + values[i], bag)))


if __name__ == "__main__":
    weights = [10, 10, 10]
    values = [2, 4, 8]
    print(process1(weights, values, 0, 0, 0, 10))
