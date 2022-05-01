from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
import bisect
from collections import namedtuple


# 从sorteddict中返回小于等于key的数，时间复杂o度为O（(logN)^2）
def floorkey(sorteddict, key):
    return None if bisect.bisect(sorteddict, key) == 0 else sorteddict[bisect.bisect(sorteddict, key) - 1]


#     0  1  2  3  4  5  6
arr = [1, 3, 5, 7, 9, 11]
for i in range(13):
    print(i, "left", bisect.bisect_left(arr, i))
    # print(i, "right", bisect.bisect(arr, i))

# USER = namedtuple('user', 'name id')
#
# user1 = USER('b', 7)
# user2 = USER('d', 5)
# user3 = USER('e', 3)
# user4 = USER('g', 5)
# sortsetname = SortedSet(key=lambda x: (x.id, x.name))
# sortsetname.add(user1)
# sortsetname.add(user2)
# sortsetname.add(user3)
# sortsetname.add(user4)
# print(sortsetname)
# print(floorkey(sortsetname, USER('d', 6)))
# sortsetid = SortedSet(key=lambda x: x.id)
# sortsetid.add(user1)
# sortsetid.add(user2)
# sortsetid.add(user3)
# print(sortsetid)
