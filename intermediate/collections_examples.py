# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaabbbbbccccccdddddd"
myCounter = Counter(a)
print(myCounter)  # Counter({'c': 6, 'd': 6, 'a': 5, 'b': 5})
mostCommon = myCounter.most_common(2)
print(mostCommon)  # [('c', 6), ('d', 6)]
print(list(map(lambda x: x[0], mostCommon)))  # ['c', 'd']

# namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)  # Point(x=1, y=-4)
print(pt.x, pt.y)  # 1 -4

# OrderedDict
# less relevant since Python 3.7, where dictionaries are ordered by default
orderedDict = OrderedDict()
orderedDict["a"] = 1
orderedDict["b"] = 2
orderedDict["c"] = 3
orderedDict["d"] = 4
print(orderedDict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# defaultdict
d = defaultdict(int)  # Args: float, list, set, tuple, dict
d["a"] = 1
d["b"] = 2
print(d["c"])  # 0, default value for the datatype of the defaultdict

# deque
d = deque()

d.append(1)
d.append(2)  # deque([1, 2])

d.appendleft(3)  # deque([3, 1, 2])

d.pop()  # deque([3, 1])

d.popleft()  # deque([1])

d.extend([2, 3, 4])  # deque([1, 2, 3, 4])

d.extendleft([0, -1, -2])  # deque([-2, -1, 0, 1, 2, 3, 4])

d.rotate(1)  # deque([4, -2, -1, 0, 1, 2, 3])
