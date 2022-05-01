# 比较器，重载比较运算符
# 对于任意的比较器，首先需要指定两个数o1,o2
# 对返回值有统一的规范
# 返回负数时，认为o1应该排在o2的前面
# 返回正数时，认为o2应该排在o1的前面
# 返回0 时，  谁排在前面都可以

# 例子1————官方给的是从小到大排序
a = [4, 5, 6, 9, 8, 2, 4, 6, 3, 8, 4]
b = sorted(a)
a.sort()
print(a)  # 输出：[2, 3, 4, 4, 4, 5, 6, 6, 8, 8, 9]
print(b)  # 输出：[2, 3, 4, 4, 4, 5, 6, 6, 8, 8, 9]

# 例子2————比较器实现从大到小排序
import functools


def myCom_number(o1, o2):
    return o2 - o1


c = [4, 5, 6, 9, 8, 2, 4, 6, 3, 8, 4]
c.sort(key=functools.cmp_to_key(myCom_number))
print(c)


# 输出：[9, 8, 8, 6, 6, 5, 4, 4, 4, 3, 2]

# 例子3：定义一个学生类，对学生排序
class Student(object):
    def __init__(self, name, age, classNo):
        self.name = name
        self.age = age
        self.classNo = classNo

    def __str__(self):
        return ('{},{},{}'.format(self.name, self.age, self.classNo))

    # 年龄按照从小到大排序
    def myCom_age(o1, o2):
        return o1.age - o2.age

    # 先按照班级排好，再按照年龄从大到小排好
    def myCom_No_age(o1, o2):
        if o1.classNo != o2.classNo:
            return o1.classNo - o2.classNo
        return o2.age - o2.age


stu1 = Student('摸鱼人生', 16, 1)
stu2 = Student('尾号9536', 18, 2)
stu3 = Student('奔跑', 12, 1)
stu4 = Student('没落', 25, 2)
arrs = [stu1, stu2, stu3, stu4]
print("--------------年龄按照从小到大排序-----------------")
b = sorted(arrs, key=functools.cmp_to_key(Student.myCom_age))
for j in range(len(b)):
    print(b[j])
# '''
# 奔跑,12,1
# 摸鱼人生,16,1
# 尾号9536,18,2
# 没落,25,2
# '''
print("--------------先按照班级排好，再按照年龄从大到小排好-----------------")
arrs.sort(key=functools.cmp_to_key(Student.myCom_No_age))
for i in range(len(arrs)):
    print(arrs[i])
# '''
# 摸鱼人生,16,1
# 奔跑,12,1
# 尾号9536,18,2
# 没落,25,2
# '''
