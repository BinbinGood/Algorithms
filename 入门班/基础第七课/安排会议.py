# 一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
# 给你每一个项目开始的时间和结束的时间(给你一个数 组，里面是一个个具体
# 的项目)，你来安排宣讲的日程，要求会议室进行的宣讲的场次最多。
# 返回这个最多的宣讲场次。

class program():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def bestArrange(programs, timepoint):
    programs.sort()
    result = []
    for program in programs:
        if timepoint < program.start:
            result.append(program)
            timepoint = program.end
    return result


