# 公司的每个员工都符合 Employee 类的描述。整个公司的人员结构可以看作是一棵标准的、 没有环的
# 多叉树。树的头节点是公司唯一的老板。除老板之外的每个员工都有唯一的直接上级。 叶节点是没有
# 任何下属的基层员工(subordinates列表为空)，除基层员工外，每个员工都有一个或多个直接下级。
# 这个公司现在要办party，你可以决定哪些员工来，哪些员工不来。但是要遵循如下规则。
# 1.如果某个员工来了，那么这个员工的所有直接下级都不能来
# 2.派对的整体快乐值是所有到场员工快乐值的累加
# 3.你的目标是让派对的整体快乐值尽量大
class Employee():
    def __init__(self, happy, nexts=None):
        self.happy = happy
        self.nexts = nexts  # 表示其有多少直接下级


def maxHappy(boss):
    if boss is None:
        return -1
    bosshappy = process(boss)
    return max(bosshappy[0], bosshappy[1])


# 返回类型：[该员工来整棵树的最大快乐值，该员工不来整棵树的最大快乐值]
def process(employee):
    if employee.nexts is None:
        return [employee.happy, 0]
    laimaxhappy = employee.happy
    bulaimaxhappy = 0
    for emp in employee.nexts:
        emphapppy = process(emp)
        laimaxhappy += emphapppy[1]
        bulaimaxhappy += max(emphapppy[0], emphapppy[1])
    return [laimaxhappy, bulaimaxhappy]


if __name__ == "__main__":
    em100 = Employee(100)
    em3 = Employee(3, [em100])
    em5 = Employee(5)
    em4 = Employee(4)
    em50 = Employee(50, [em5, em4])
    em7 = Employee(7)
    em100 = Employee(100, [em7])
    boss = Employee(5, [em3, em50, em100])
    print(maxHappy(boss))
