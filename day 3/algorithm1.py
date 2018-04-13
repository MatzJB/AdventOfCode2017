'''
Puzzle 1 day three
'''
import math


def printMatrix(M):
    for row in M:
        print row
    print

length = 1  # the length of the 'snake'
myNumber = 25

m = int(math.ceil(math.sqrt(myNumber)))
M = [[0] * m for i in range(m)]
M[2][1:5] = [2 for i in [0] * 4]

M[1:5][2] = [3] * 4

printMatrix(M)
# coord = round(m / 2)
exit(0)

coord = [m / 2, m / 2]
coord = map(round, coord)

theta = 0
index = 1
for i in range(8):
    theta = i * math.pi / 2
    direction = map(int, [math.cos(theta), math.sin(theta)])
    coord += direction
    M[int(coord[1])][int(coord[2])] = index

    index = index + 1
    print direction

printMatrix(M)
