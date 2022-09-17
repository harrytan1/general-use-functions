# euclidian distance given 2 arrays of size n
import numpy as np

def ed(p1, p2):
    print(np.linalg.norm(p1 - p2))

start = np.array((0, 0, 0, 0))

p1 = np.array((3, 10, 2, 11))
p2 = np.array((17, -17, 9, -1))
p3 = np.array((-4, 9, -2, -1))
p4 = np.array((4, 0, 2, -5))
p5 = np.array((8, -1, 6, -12))
p6 = np.array((19, 3, 23, 14))

ed(start, p1)
ed(start, p2)
ed(start, p3)
ed(start, p4)
ed(start, p5)
ed(start, p6)