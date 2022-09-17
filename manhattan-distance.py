
def md(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += abs(p1[i] - p2[i])
    print(dist)

start = [0,0,0,0]
p1 = [3, 10, 2, 11]
p2 = [17, -17, 9, -1]
p3 = [-4, 9, -2, -1]
p4 = [4, 0, 2, -5]
p5 = [8, -1, 6, -12]
p6 = [19, 3, 23, 14]

md(start, p1)
md(start, p2)
md(start, p3)
md(start, p4)
md(start, p5)
md(start, p6)